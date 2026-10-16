# Paper trading — signal for the close of 2026-10-16
_Generated 2026-10-16 19:50 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% SOXL (3x SOXX) — overnight
- 25% TECL (3x XLK) — overnight
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight

SOXX above 200-day MA: **True**. Leg M' picks: **LITE, MU, SNDK, MRVL, INTC**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
MU     27765.2      True     49.2
NVDA   23914.1      True     20.5
META   16078.5      True      5.5
SNDK   13729.5      True     49.2
AMD    12955.8      True     19.0
SPCX   12815.9     False      NaN
TSLA   12723.5     False     -6.9
AAPL   12489.1      True      2.6
INTC   11792.5      True     31.7
MSFT   11589.7      True      3.4
AMZN    9045.3      True     11.6
GOOGL   8687.7      True      8.0
AVGO    7924.6     False     19.1
GOOG    5548.3     False      5.6
MRVL    5330.2      True     47.8
TSM     4771.0      True     22.8
LITE    4698.7      True     61.0
PLTR    4493.0      True     10.0
ORCL    4213.6     False      1.6
NBIS    4095.1     False     40.3
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 5 | -23.5% | -21.1% | -3.0 -6.7 -3.4 -5.5 -4.5 |
| LegM | 5 | -16.2% | -10.5% | -2.1 -5.6 +0.0 +0.0 -3.2 |
| V6A | 5 | -23.5% | -21.1% | -3.0 -6.7 -3.4 -5.5 -4.5 |
| LegMA | 5 | -16.2% | -10.5% | -2.1 -5.6 +0.0 +0.0 -3.2 |
| V8 | 5 | -13.7% | -10.9% | -2.3 -5.6 +0.0 +0.0 -3.4 |
| V7 | 5 | -17.7% | -12.1% | -2.1 -5.6 -1.6 -0.2 -3.2 |
