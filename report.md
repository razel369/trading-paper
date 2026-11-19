# Paper trading — signal for the close of 2026-11-18
_Generated 2026-11-18 21:47 New York time. Research only, not investment advice._

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
- 25% UPRO (3x SPY) — overnight
- 25% FAS (3x XLF) — overnight
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
NVDA   44014.7     False     13.9
MU     25045.4     False     45.4
AMD    18937.3      True     21.4
AAPL   16637.1      True      1.0
SPCX   14922.0     False      NaN
MSFT   14728.1      True      5.0
TSLA   14351.5      True     -2.5
META   13991.2     False      9.0
AMZN   12878.2      True      8.8
SNDK   12686.7     False     44.7
GOOGL  12311.8     False      1.5
INTC    9661.6     False     20.5
AVGO    9351.3     False     20.6
GOOG    7997.8     False     -0.9
TSM     6067.3     False     23.3
MRVL    5408.6     False     42.0
ORCL    5172.8     False      3.6
LITE    4411.7     False     45.5
LLY     4256.3      True     22.5
PLTR    4228.2      True      6.7
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 28 | -21.7% | -19.5% | +0.0 +0.0 -2.5 -0.1 +0.5 |
| LegM | 28 | -13.3% | -9.6% | +0.0 +0.0 -4.9 -0.1 +0.9 |
| V6A | 28 | -20.6% | -18.3% | +0.0 +0.0 -2.2 +0.0 +0.1 |
| LegMA | 28 | -10.9% | -7.0% | +0.0 +0.0 -4.3 +0.1 +0.3 |
| V8 | 28 | -9.0% | -7.1% | +0.0 +0.0 -2.7 -0.8 -0.1 |
| V7 | 28 | -16.5% | -13.0% | +0.1 +0.0 -4.9 -0.1 +0.9 |
