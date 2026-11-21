# Paper trading — signal for the close of 2026-11-20
_Generated 2026-11-20 21:48 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- cash

**LegM** — Leg M' 100% (blind-passed)
- cash

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- cash

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- cash

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% FAS (3x XLF) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- trend SPY: exposure +14% of capital (long via UPRO / short via SPXU; divide by fund leverage) — hold
- trend QQQ: exposure +9% of capital (long via TQQQ / short via SQQQ; divide by fund leverage) — hold
- trend IWM: exposure +12% of capital (long via TNA / short via TZA; divide by fund leverage) — hold
- trend TLT: exposure -22% of capital (long via TMF / short via TMV; divide by fund leverage) — hold
- trend IEF: exposure -37% of capital (long via TYD / short via TYO; divide by fund leverage) — hold
- trend GLD: exposure -9% of capital (long via UGL / short via GLL; divide by fund leverage) — hold
- trend SLV: exposure -6% of capital (long via AGQ / short via ZSL; divide by fund leverage) — hold
- trend DBC: exposure +13% of capital (long via DBC / short via -; divide by fund leverage) — hold
- trend USO: exposure +6% of capital (long via UCO / short via SCO; divide by fund leverage) — hold
- trend UUP: exposure +47% of capital (long via UUP / short via UDN; divide by fund leverage) — hold
- trend EFA: exposure +15% of capital (long via EFA / short via EFZ; divide by fund leverage) — hold
- trend EEM: exposure +9% of capital (long via EDC / short via EDZ; divide by fund leverage) — hold
- trend VNQ: exposure +15% of capital (long via DRN / short via DRV; divide by fund leverage) — hold
- trend FXE: exposure -49% of capital (long via ULE / short via EUO; divide by fund leverage) — hold
- trend FXY: exposure -29% of capital (long via YCL / short via YCS; divide by fund leverage) — hold
- trend XLE: exposure +9% of capital (long via ERX / short via ERY; divide by fund leverage) — hold

SOXX above 200-day MA: **False**. Leg M' picks: **none (cash)**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
NVDA   48161.6     False     11.6
MU     25726.1     False     44.6
AMD    21081.5     False     18.7
AAPL   17228.8      True      1.1
MSFT   15663.9      True      5.1
SPCX   14307.3     False      NaN
TSLA   14032.8     False     -4.0
AMZN   13552.1      True      8.3
META   13377.3     False      7.8
GOOGL  13021.5     False      0.9
AVGO   10001.6     False     20.1
INTC    9682.9     False     20.7
GOOG    8386.5     False     -1.6
TSM     6440.5     False     21.8
MRVL    5436.8     False     40.9
ORCL    5215.5     False      3.5
LLY     4392.9      True     22.7
LITE    4270.4     False     41.3
PLTR    4257.0     False      5.0
NBIS    4020.4     False     23.9
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 30 | -21.2% | -19.2% | -2.5 -0.1 +0.5 +1.5 -1.1 |
| LegM | 30 | -12.4% | -9.0% | -4.9 -0.1 +0.9 +3.0 -2.3 |
| V6A | 30 | -20.8% | -18.7% | -2.2 +0.0 +0.1 +0.1 -0.6 |
| LegMA | 30 | -11.4% | -8.0% | -4.3 +0.1 +0.3 +0.2 -1.3 |
| V8 | 30 | -9.0% | -7.4% | -2.7 -0.8 -0.1 +0.9 -1.3 |
| V7 | 30 | -15.6% | -12.4% | -4.9 -0.1 +0.9 +3.0 -2.3 |
