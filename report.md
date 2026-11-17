# Paper trading — signal for the close of 2026-11-16
_Generated 2026-11-16 23:10 New York time. Research only, not investment advice._

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
NVDA   40055.1     False     12.8
MU     24749.7     False     43.4
AMD    18004.1      True     19.6
AAPL   16521.6      True      1.0
SPCX   16297.0     False      NaN
TSLA   14958.0     False     -3.2
META   14879.8     False      8.1
MSFT   14219.9      True      4.1
AMZN   12696.2      True      7.9
SNDK   12483.8     False     43.9
GOOGL  12275.3     False      2.0
INTC    9881.5     False     20.0
AVGO    8984.2     False     19.6
GOOG    7977.8     False     -0.5
TSM     5890.4     False     21.8
MRVL    5430.3     False     38.6
ORCL    5282.0     False      2.2
LITE    4531.3     False     45.0
PLTR    4334.9      True      5.8
LLY     4179.5      True     22.8
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 26 | -21.9% | -19.8% | -0.7 +0.0 +0.0 +0.0 -2.5 |
| LegM | 26 | -13.9% | -10.3% | -1.4 +0.0 +0.0 +0.0 -4.9 |
| V6A | 26 | -20.8% | -18.4% | -0.2 +0.0 +0.0 +0.0 -2.2 |
| LegMA | 26 | -11.2% | -7.3% | -0.5 +0.0 +0.0 +0.0 -4.3 |
| V8 | 26 | -8.2% | -6.3% | -1.5 +0.0 +0.0 +0.0 -2.7 |
| V7 | 26 | -17.1% | -13.6% | -1.4 +1.8 +0.1 +0.0 -4.9 |
