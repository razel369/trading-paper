# Paper trading — signal for the close of 2026-10-23
_Generated 2026-10-23 19:58 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% MRVL (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight
- 10% MRNA (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% MRVL (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight
- 20% MRNA (1x, no 2x fund) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% MRVL (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight
- 10% MRNA (1x, no 2x fund) — overnight
- 50% SOXL (3x SOXX) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% MRVL (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight
- 20% MRNA (1x, no 2x fund) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% SOXL (3x SOXX) — overnight
- 25% TECL (3x XLK) — overnight
- 10% MRVL (1x, no 2x fund) — overnight
- 10% MUU (2x MU) — overnight
- 10% SNDK (1x, no 2x fund) — overnight
- 10% LINT (2x INTC) — overnight
- 10% MRNA (1x, no 2x fund) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% MRVL (1x, no 2x fund) — overnight
- 20% MUU (2x MU) — overnight
- 20% SNDK (1x, no 2x fund) — overnight
- 20% LINT (2x INTC) — overnight
- 20% MRNA (1x, no 2x fund) — overnight

SOXX above 200-day MA: **True**. Leg M' picks: **MRVL, MU, SNDK, INTC, MRNA**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
MU     26570.0      True     48.2
NVDA   23759.4      True     20.3
SPCX   15752.4     False      NaN
META   13747.1      True      2.4
TSLA   13390.8     False     -5.3
AAPL   13061.8      True      1.2
SNDK   12175.3      True     47.2
AMD    11402.6      True     17.5
MSFT   10632.2      True      2.3
INTC   10164.8      True     30.0
AMZN    9113.7      True     11.4
GOOGL   8118.2     False      5.7
AVGO    7561.8     False     17.0
MRVL    5299.0      True     49.6
GOOG    5286.3     False      3.4
TSM     5016.1      True     21.5
LITE    4662.2     False     60.5
PLTR    4343.7      True      8.1
MRNA    4162.8      True     22.2
NBIS    4067.4     False     36.7
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 10 | -20.5% | -19.3% | +8.7 -2.1 +2.7 -6.2 -0.3 |
| LegM | 10 | -7.9% | -4.6% | +6.6 +0.0 +0.0 +0.0 +0.0 |
| V6A | 10 | -20.5% | -19.3% | +8.7 -2.1 +2.7 -6.2 -0.3 |
| LegMA | 10 | -7.9% | -4.6% | +6.6 +0.0 +0.0 +0.0 +0.0 |
| V8 | 10 | -5.9% | -4.2% | +7.5 +0.0 +0.0 +0.0 +0.0 |
| V7 | 10 | -10.1% | -6.9% | +6.6 +0.3 +0.2 -1.8 +0.7 |
