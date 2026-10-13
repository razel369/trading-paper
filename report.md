# Paper trading — signal for the close of 2026-10-12
_Generated 2026-10-12 22:42 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% BE (1x, no 2x fund) — overnight
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% BE (1x, no 2x fund) — overnight
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% BE (1x, no 2x fund) — overnight
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% BE (1x, no 2x fund) — overnight
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% SOXL (3x SOXX) — overnight
- 25% TECL (3x XLK) — overnight
- 10% BE (1x, no 2x fund) — overnight
- 10% LITE (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% MRVL (1x, no 2x fund) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% BE (1x, no 2x fund) — overnight
- 20% LITE (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% MRVL (1x, no 2x fund) — overnight

SOXX above 200-day MA: **True**. Leg M' picks: **BE, LITE, MU, SNDK, MRVL**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
MU     26727.2      True     56.2
NVDA   24079.6      True     23.1
META   15958.4      True      6.4
SPCX   14913.1     False      NaN
SNDK   14442.6      True     54.9
AMD    13043.2      True     25.1
TSLA   13004.1     False     -6.5
AAPL   12454.3      True      0.9
INTC   12359.6      True     35.3
MSFT   11329.3      True      2.5
AMZN    9254.7      True     11.4
GOOGL   8806.1      True      7.7
AVGO    8258.9     False     22.4
GOOG    5688.2      True      5.2
MRVL    5101.2      True     53.4
LITE    4808.0      True     66.7
BE      4520.8      True     67.6
PLTR    4510.6      True     11.5
TSM     4399.5      True     26.6
ORCL    4210.6     False      3.3
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 1 | -3.4% | -3.0% | -3.0 |
| LegM | 1 | -3.1% | -2.1% | -2.1 |
| V6A | 1 | -3.4% | -3.0% | -3.0 |
| LegMA | 1 | -3.1% | -2.1% | -2.1 |
| V8 | 1 | -2.8% | -2.3% | -2.3 |
| V7 | 1 | -3.1% | -2.1% | -2.1 |
