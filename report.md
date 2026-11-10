# Paper trading — signal for the close of 2026-11-09
_Generated 2026-11-09 22:47 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% AMDL (2x AMD) — overnight
- 10% METU (2x META) — overnight
- 10% AMZU (2x AMZN) — overnight
- 10% MSFU (2x MSFT) — overnight
- 10% PLTU (2x PLTR) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% AMDL (2x AMD) — overnight
- 20% METU (2x META) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight
- 20% PLTU (2x PLTR) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% AMDL (2x AMD) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% AMDL (2x AMD) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% TECL (3x XLK) — overnight
- 25% UDOW (3x DIA) — overnight
- 10% AMDL (2x AMD) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% AMDL (2x AMD) — overnight
- 20% METU (2x META) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight
- 20% PLTU (2x PLTR) — overnight

SOXX above 200-day MA: **False**. Leg M' picks: **AMD, META, AMZN, MSFT, PLTR**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
NVDA   27696.2     False     15.7
MU     26062.4     False     45.2
AAPL   17137.3      True     -0.6
META   16191.7      True      7.6
SPCX   16005.9     False      NaN
TSLA   15385.3     False     -5.8
AMD    14799.6      True     19.5
MSFT   13819.7      True      3.7
SNDK   12660.1     False     44.7
AMZN   12621.0      True      7.0
GOOGL  12102.9     False      0.6
INTC   11019.2     False     20.8
AVGO    8130.5     False     18.0
GOOG    7981.8     False     -1.9
TSM     6089.1     False     21.8
MRVL    5745.4     False     39.7
ORCL    5617.5     False     -0.1
LITE    4939.4     False     47.9
PLTR    4882.3      True      2.6
NBIS    4118.5     False     32.1
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 21 | -19.5% | -17.2% | +0.2 +0.0 +0.0 +9.7 +0.0 |
| LegM | 21 | -8.3% | -4.4% | +0.4 +0.0 +0.0 +0.0 +0.0 |
| V6A | 21 | -18.8% | -16.4% | +1.1 +0.0 +0.0 +9.7 +0.0 |
| LegMA | 21 | -6.8% | -2.6% | +2.2 +0.0 +0.0 +0.0 +0.0 |
| V8 | 21 | -4.3% | -2.2% | +1.2 +0.0 +0.0 +0.0 +0.0 |
| V7 | 21 | -13.4% | -9.7% | +0.4 +0.3 -4.2 +1.1 +1.4 |
