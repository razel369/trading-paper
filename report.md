# Paper trading — signal for the close of 2026-11-02
_Generated 2026-11-02 22:02 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% MUU (2x MU) — overnight
- 10% AMDL (2x AMD) — overnight
- 10% PLTU (2x PLTR) — overnight
- 10% AMZU (2x AMZN) — overnight
- 10% MSFU (2x MSFT) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% MUU (2x MU) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% PLTU (2x PLTR) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% MUU (2x MU) — overnight
- 10% AMDL (2x AMD) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% MUU (2x MU) — overnight
- 20% AMDL (2x AMD) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% TECL (3x XLK) — overnight
- 25% UDOW (3x DIA) — overnight
- 10% MUU (2x MU) — overnight
- 10% AMDL (2x AMD) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% MUU (2x MU) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% PLTU (2x PLTR) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight

SOXX above 200-day MA: **False**. Leg M' picks: **MU, AMD, PLTR, AMZN, MSFT**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
MU     25016.7      True     43.9
NVDA   22011.5     False     17.1
META   15679.6     False      4.5
SPCX   15452.2     False      NaN
AAPL   14349.2      True     -0.9
TSLA   13890.6      True     -4.2
SNDK   12147.8     False     40.9
AMD    11922.9      True     12.5
MSFT   11862.2      True      1.2
INTC   10835.4     False     19.7
GOOGL  10811.9     False     -2.2
AMZN   10750.6      True      1.8
AVGO    7609.9     False     15.6
GOOG    6993.5     False     -4.4
MRVL    6028.8     False     39.4
TSM     5187.5     False     18.7
LITE    5107.8     False     56.2
PLTR    4711.2      True      5.0
ORCL    4495.0     False     -2.5
NBIS    4224.8     False     29.5
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 16 | -26.2% | -24.6% | +2.5 +1.4 -2.8 -10.1 +1.5 |
| LegM | 16 | -9.0% | -4.8% | +0.0 +0.0 +0.0 +0.0 +0.0 |
| V6A | 16 | -26.2% | -24.6% | +2.5 +1.4 -2.8 -10.1 +1.5 |
| LegMA | 16 | -9.0% | -4.8% | +0.0 +0.0 +0.0 +0.0 +0.0 |
| V8 | 16 | -5.4% | -3.3% | +0.0 +0.0 +0.0 +0.0 +0.0 |
| V7 | 16 | -12.7% | -8.7% | +0.5 +0.5 -0.0 -1.8 -0.9 |
