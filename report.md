# Paper trading — signal for the close of 2026-10-15
_Generated 2026-10-15 19:49 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% LITE (1x, no 2x fund) — overnight
- 10% BE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% LITE (1x, no 2x fund) — overnight
- 20% BE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% LITE (1x, no 2x fund) — overnight
- 10% BE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% LITE (1x, no 2x fund) — overnight
- 20% BE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% SOXL (3x SOXX) — overnight
- 25% TECL (3x XLK) — overnight
- 10% LITE (1x, no 2x fund) — overnight
- 10% BE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% LITE (1x, no 2x fund) — overnight
- 20% BE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

SOXX above 200-day MA: **True**. Leg M' picks: **LITE, BE, MU, SNDK, MRVL**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
MU     28223.9      True     49.7
NVDA   24733.3      True     20.3
META   16254.0      True      5.2
SNDK   14738.4      True     49.1
SPCX   14713.9     False      NaN
AMD    13247.0      True     19.8
AAPL   12913.7      True      2.2
TSLA   12570.4     False     -7.9
INTC   12192.2      True     32.0
MSFT   11912.1      True      3.1
AMZN    9213.8      True     11.5
GOOGL   9032.2      True      8.0
AVGO    8219.5     False     19.3
GOOG    5839.3      True      5.5
MRVL    5373.4      True     48.3
LITE    4955.0      True     61.1
TSM     4706.4      True     22.7
BE      4594.9      True     60.1
PLTR    4533.8      True      9.5
ORCL    4271.1     False      0.7
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 4 | -19.2% | -17.4% | -3.0 -6.7 -3.4 -5.5 |
| LegM | 4 | -11.7% | -7.5% | -2.1 -5.6 +0.0 +0.0 |
| V6A | 4 | -19.2% | -17.4% | -3.0 -6.7 -3.4 -5.5 |
| LegMA | 4 | -11.7% | -7.5% | -2.1 -5.6 +0.0 +0.0 |
| V8 | 4 | -9.8% | -7.8% | -2.3 -5.6 +0.0 +0.0 |
| V7 | 4 | -13.3% | -9.2% | -2.1 -5.6 -1.6 -0.2 |
