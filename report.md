# Paper trading — signal for the close of 2026-11-19
_Generated 2026-11-19 21:34 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight
- 10% AMZU (2x AMZN) — overnight
- 10% MSFU (2x MSFT) — overnight
- 10% V (1x, no 2x fund) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight
- 20% V (1x, no 2x fund) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% FAS (3x XLF) — overnight
- 25% LABU (3x XBI) — overnight
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight
- 20% V (1x, no 2x fund) — overnight

SOXX above 200-day MA: **False**. Leg M' picks: **LLY, AMD, AMZN, MSFT, V**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
NVDA   45058.9     False     12.4
MU     24888.1     False     46.7
AMD    19974.8      True     20.6
AAPL   16535.6      True      0.7
MSFT   14873.2      True      5.4
TSLA   13881.6     False     -2.9
AMZN   12952.1      True      8.7
GOOGL  12535.0     False      1.6
INTC    9462.2     False     21.6
AVGO    9349.3     False     20.3
TSM     6044.8     False     22.7
MRVL    5338.3     False     42.6
ORCL    5096.6     False      3.6
LLY     4299.1      True     22.2
STX     3426.2     False     26.9
AMAT    3004.5     False     28.0
V       2981.0      True      2.0
LRCX    2903.5     False     37.0
WMT     2820.7      True     -4.0
WDC     2621.3     False     18.5
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 28 | -21.7% | -19.5% | +0.0 +0.0 -2.5 -0.1 +0.5 |
| LegM | 28 | -13.3% | -9.6% | +0.0 +0.0 -4.9 -0.1 +0.9 |
| V6A | 29 | -20.4% | -18.2% | +0.0 -2.2 +0.0 +0.1 +0.1 |
| LegMA | 29 | -10.4% | -6.8% | +0.0 -4.3 +0.1 +0.3 +0.2 |
| V8 | 29 | -8.0% | -6.2% | +0.0 -2.7 -0.8 -0.1 +0.9 |
| V7 | 28 | -16.5% | -13.0% | +0.1 +0.0 -4.9 -0.1 +0.9 |
