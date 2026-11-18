# Paper trading — signal for the close of 2026-11-17
_Generated 2026-11-17 22:07 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight
- 10% AMZU (2x AMZN) — overnight
- 10% PLTU (2x PLTR) — overnight
- 10% MSFU (2x MSFT) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% PLTU (2x PLTR) — overnight
- 20% MSFU (2x MSFT) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% UDOW (3x DIA) — overnight
- 25% UPRO (3x SPY) — overnight
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% PLTU (2x PLTR) — overnight
- 20% MSFU (2x MSFT) — overnight

SOXX above 200-day MA: **False**. Leg M' picks: **LLY, AMD, AMZN, PLTR, MSFT**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
NVDA   42310.9     False     13.7
MU     25027.9     False     44.8
AMD    18530.2      True     20.9
AAPL   16647.2      True      0.7
SPCX   16059.4     False      NaN
TSLA   14780.1     False     -2.5
META   14688.7     False      8.6
MSFT   14539.3      True      4.8
AMZN   12736.4      True      8.7
SNDK   12656.3     False     45.3
GOOGL  12413.5     False      1.6
INTC    9789.9     False     20.3
AVGO    9178.5     False     19.8
GOOG    8012.6     False     -0.9
TSM     6076.9     False     22.3
MRVL    5441.6     False     41.3
ORCL    5254.2     False      2.9
LITE    4479.1     False     46.0
PLTR    4327.0      True      6.4
LLY     4176.3      True     22.7
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 27 | -22.0% | -19.8% | +0.0 +0.0 +0.0 -2.5 -0.1 |
| LegM | 27 | -14.1% | -10.5% | +0.0 +0.0 +0.0 -4.9 -0.1 |
| V6A | 27 | -20.7% | -18.4% | +0.0 +0.0 +0.0 -2.2 +0.0 |
| LegMA | 27 | -11.1% | -7.3% | +0.0 +0.0 +0.0 -4.3 +0.1 |
| V8 | 27 | -8.9% | -7.0% | +0.0 +0.0 +0.0 -2.7 -0.8 |
| V7 | 27 | -17.2% | -13.8% | +1.8 +0.1 +0.0 -4.9 -0.1 |
