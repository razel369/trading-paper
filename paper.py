"""Paper trading for the lab strategies (V6, Leg M' alone, V7). Runs once per weekday after the US close.

Each run:
  1. downloads ~3 years of daily bars (yfinance) for the candidate universe, SOXX/SOXL, 2x funds and trend ETFs;
  2. settles every open decision whose next session now exists (model return and real-instrument return);
  3. records tonight's decision for each strategy (fills assumed at today's close, exit at the next open
     for overnight legs, next close for trend legs);
  4. rewrites report.md.
With --preview (run ~15:35 New York time) it only writes signal_preview.md from intraday prices, for placing
MOC orders before the 15:50 cutoff; nothing is journaled.
"""
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import yfinance as yf

HERE = Path(__file__).parent
NY = ZoneInfo("America/New_York")
U = json.loads((HERE / "universe.json").read_text())
UNIVERSE, LEV2X = U["universe"], U["lev2x"]
TREND = ["SPY", "QQQ", "IWM", "TLT", "IEF", "GLD", "SLV", "DBC", "USO", "UUP", "EFA", "EEM", "VNQ", "FXE", "FXY", "XLE"]
TREND_FUNDS = {"SPY": ("UPRO", "SPXU"), "QQQ": ("TQQQ", "SQQQ"), "IWM": ("TNA", "TZA"), "TLT": ("TMF", "TMV"),
               "IEF": ("TYD", "TYO"), "GLD": ("UGL", "GLL"), "SLV": ("AGQ", "ZSL"), "DBC": ("DBC", "-"),
               "USO": ("UCO", "SCO"), "UUP": ("UUP", "UDN"), "EFA": ("EFA", "EFZ"), "EEM": ("EDC", "EDZ"),
               "VNQ": ("DRN", "DRV"), "FXE": ("ULE", "EUO"), "FXY": ("YCL", "YCS"), "XLE": ("ERX", "ERY")}
COST, FEE2, FEE3 = 0.0005, 0.01 / 252, 0.0095 / 252
STRATS = {"V6": "50% SOXL + 50% Leg M' (blind-passed)", "LegM": "Leg M' 100% (blind-passed)",
          "V7": "Leg M', trend sleeve when idle (withdrawn, comparison)"}
JOURNAL, EQUITY = HERE / "journal.json", HERE / "equity.csv"


def download():
    tick = sorted(set(UNIVERSE) | {"SOXX", "SOXL"} | set(LEV2X.values()) | set(TREND))
    raw = yf.download(tick, period="3y", auto_adjust=True, progress=False, group_by="ticker", threads=True)
    f = {k: pd.DataFrame({t: raw[t][k] for t in tick if t in raw.columns.get_level_values(0)})
         for k in ["Open", "High", "Low", "Close", "Volume"]}
    for k in f:
        f[k].index = pd.to_datetime(f[k].index).tz_localize(None)
    return f


def drop_partial(f, preview):
    now = datetime.now(NY)
    last = f["Close"].index[-1]
    if not preview and last.date() == now.date() and (now.hour, now.minute) < (16, 20):
        f = {k: v.iloc[:-1] for k, v in f.items()}       # today's bar is still live
    return f


def leg_m(f, n_univ=20, n_pick=5):
    """Leg M' at the last bar: top-20 by 20d $vol (price >= $5), close > SMA200, best 5 by 250-night mean overnight."""
    C, O, V = f["Close"][UNIVERSE], f["Open"][UNIVERSE], f["Volume"][UNIVERSE]
    dv = (C * V).rolling(20, min_periods=20).mean().iloc[-1]
    ma = C.rolling(200, min_periods=200).mean().iloc[-1]
    on_past = (O / C.shift(1) - 1).clip(-0.5, 1.0)
    m250 = on_past.rolling(250, min_periods=200).mean().iloc[-1]
    c = C.iloc[-1]
    ok = dv.notna() & (c >= 5)
    univ = dv[ok].sort_values(ascending=False).index[:n_univ]
    q = [t for t in univ if c[t] > ma[t] and pd.notna(m250[t])]
    table = pd.DataFrame({"dv20_$M": dv[univ] / 1e6, "above200": [c[t] > ma[t] for t in univ], "m250_bp": m250[univ] * 1e4})
    if len(q) < n_pick:
        return [], table
    return list(m250[q].sort_values(ascending=False).index[:n_pick]), table


def soxx_up(f):
    c = f["Close"]["SOXX"].dropna()
    return bool(c.iloc[-1] > c.rolling(200).mean().iloc[-1])


def trend_weights(f):
    """trend.py (Moskowitz–Ooi–Pedersen params) at the last bar, then x2 with gross <= 3."""
    c = f["Close"][TREND].ffill(limit=3)
    sig = np.sign(c.iloc[-1] / c.iloc[-253] - 1)
    vol = c.pct_change().iloc[-60:].std() * np.sqrt(252)
    w = (sig * 0.10 / vol).clip(-3, 3).dropna()
    n = len(w)
    w = w / n * np.sqrt(n) * 2.0
    g = w.abs().sum()
    return (w * min(1.0, 3.0 / g)) if g > 0 else w


def decide(f, state):
    picks, table = leg_m(f)
    up = soxx_up(f)
    # trend sleeve: rebalance every 5 trading days, otherwise keep last weights
    d = f["Close"].index[-1]
    tw = state.get("trend")
    if tw is None or len(f["Close"].loc[pd.Timestamp(tw["date"]):].index) - 1 >= 5:
        tw = {"date": str(d.date()), "w": {k: round(float(v), 4) for k, v in trend_weights(f).items()}}
        state["trend"] = tw
    pos_m = lambda wt: [{"und": t, "instr": LEV2X.get(t, t), "w": wt, "lev": 2, "kind": "on"} for t in picks]
    out = {"V6": pos_m(0.10) + ([{"und": "SOXX", "instr": "SOXL", "w": 0.5, "lev": 3, "kind": "on"}] if up else []),
           "LegM": pos_m(0.20)}
    out["V7"] = pos_m(0.20) if picks else [{"und": a, "instr": a, "w": w, "lev": 1, "kind": "cc"} for a, w in tw["w"].items()]
    return out, picks, table, up


def settle(dec, f):
    """Model and real-instrument return of one decision, or None if the next session is not in the data yet."""
    d = pd.Timestamp(dec["date"]); idx = f["Close"].index
    after = idx[idx > d]
    if len(after) == 0 or d not in idx:
        return None
    n = after[0]
    O, C = f["Open"], f["Close"]
    model = instr = 0.0
    active = sum(p["w"] for p in dec["pos"] if p["kind"] == "on")
    for p in dec["pos"]:
        u, i = p["und"], p["instr"]
        if p["kind"] == "on":
            ru = O.at[n, u] / C.at[d, u] - 1
            fee = FEE3 if p["lev"] == 3 else FEE2
            model += p["w"] * (p["lev"] * ru - fee)
            ri = O.at[n, i] / C.at[d, i] - 1 if i in O and pd.notna(O.at[n, i]) and pd.notna(C.at[d, i]) else np.nan
            instr += p["w"] * (ri if pd.notna(ri) else ru)          # no fund → the stock itself (1x)
        else:
            r = C.at[n, u] / C.at[d, u] - 1
            model += p["w"] * r; instr += p["w"] * r
    cost = COST * (active + sum(abs(p["w"]) for p in dec["pos"] if p["kind"] == "cc") * 0.2)   # trend: ~1/5 turnover/day
    if any(pd.isna(x) for x in [model, instr]):
        return None
    return {"exit_date": str(n.date()), "model": round(model - cost, 6), "instr": round(instr - cost, 6)}


def write_report(state, journal, picks, table, up, d, preview=False):
    lines = [f"# {'PREVIEW (intraday, not journaled)' if preview else 'Paper trading'} — signal for the close of {d.date()}",
             f"_Generated {datetime.now(NY):%Y-%m-%d %H:%M} New York time. Research only, not investment advice._", ""]
    last = {s: [j for j in journal if j["strategy"] == s and j["date"] == str(d.date())] for s in STRATS}
    lines += ["## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)", ""]
    for s, desc in STRATS.items():
        pos = last[s][0]["pos"] if last[s] else []
        lines.append(f"**{s}** — {desc}")
        if not pos:
            lines.append("- cash")
        for p in pos:
            if p["kind"] == "on":
                lines.append(f"- {p['w']*100:.0f}% {p['instr']}" + (f" ({p['lev']}x {p['und']})" if p["instr"] != p["und"] else " (1x, no 2x fund)")
                             + " — overnight")
            else:
                lo, sh = TREND_FUNDS.get(p["und"], (p["und"], "-"))
                lines.append(f"- trend {p['und']}: exposure {p['w']*100:+.0f}% of capital (long via {lo} / short via {sh}; divide by fund leverage) — hold")
        lines.append("")
    lines += [f"SOXX above 200-day MA: **{up}**. Leg M' picks: **{', '.join(picks) or 'none (cash)'}**", "",
              "### Leg M' ranking (top-20 by 20-day dollar volume)", "", "```", table.round(1).to_string(), "```", ""]
    if not preview and EQUITY.exists():
        eq = pd.read_csv(EQUITY)
        if len(eq):
            lines += ["## Performance since start (model = synthetic leverage as in backtests; real = actual funds)", "",
                      "| strategy | nights | model | real | last 5 real |", "|---|---|---|---|---|"]
            for s in STRATS:
                e = eq[eq.strategy == s]
                if len(e):
                    lines.append(f"| {s} | {len(e)} | {(np.prod(1 + e.model) - 1)*100:+.1f}% | {(np.prod(1 + e.instr) - 1)*100:+.1f}% | "
                                 + " ".join(f"{x*100:+.1f}" for x in e.instr.tail(5)) + " |")
            lines.append("")
    (HERE / ("signal_preview.md" if preview else "report.md")).write_text("\n".join(lines))


def main():
    preview = "--preview" in sys.argv
    f = drop_partial(download(), preview)
    if "--asof" in sys.argv:                       # testing only: pretend today is that date
        a = pd.Timestamp(sys.argv[sys.argv.index("--asof") + 1])
        f = {k: v.loc[:a] for k, v in f.items()}
    d = f["Close"].index[-1]
    state = json.loads((HERE / "state.json").read_text()) if (HERE / "state.json").exists() else {}
    journal = json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
    if preview:
        dec, picks, table, up = decide(f, dict(state))
        tmp = [{"strategy": s, "date": str(d.date()), "pos": p} for s, p in dec.items()]
        write_report(state, tmp, picks, table, up, d, preview=True); print((HERE / "signal_preview.md").read_text()); return
    # 1) settle
    rows = []
    for j in journal:
        if j.get("result") is None:
            j["result"] = settle(j, f)
            if j["result"]:
                rows.append({"date": j["date"], "exit": j["result"]["exit_date"], "strategy": j["strategy"],
                             "model": j["result"]["model"], "instr": j["result"]["instr"]})
    if rows:
        new = pd.DataFrame(rows)
        old = pd.read_csv(EQUITY) if EQUITY.exists() else pd.DataFrame(columns=new.columns)
        pd.concat([old, new]).to_csv(EQUITY, index=False)
    # 2) decide for today's close (once per date)
    dec, picks, table, up = decide(f, state)
    if not any(j["date"] == str(d.date()) for j in journal):
        journal += [{"strategy": s, "date": str(d.date()), "pos": p, "result": None} for s, p in dec.items()]
    JOURNAL.write_text(json.dumps(journal, indent=1))
    (HERE / "state.json").write_text(json.dumps(state, indent=1))
    write_report(state, journal, picks, table, up, d)
    print((HERE / "report.md").read_text())


if __name__ == "__main__":
    main()
