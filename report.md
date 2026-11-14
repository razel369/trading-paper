# Paper trading — signal for the close of 2026-11-13
_Generated 2026-11-13 20:43 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 10% MUU (2x MU) — overnight
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight
- 10% AMZU (2x AMZN) — overnight
- 10% MSFU (2x MSFT) — overnight

**LegM** — Leg M' 100% (blind-passed)
- 20% MUU (2x MU) — overnight
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 10% MUU (2x MU) — overnight
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- 20% MUU (2x MU) — overnight
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- 25% UDOW (3x DIA) — overnight
- 25% UPRO (3x SPY) — overnight
- 10% MUU (2x MU) — overnight
- 10% LLYX (2x LLY) — overnight
- 10% AMDL (2x AMD) — overnight

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- 20% MUU (2x MU) — overnight
- 20% LLYX (2x LLY) — overnight
- 20% AMDL (2x AMD) — overnight
- 20% AMZU (2x AMZN) — overnight
- 20% MSFU (2x MSFT) — overnight

SOXX above 200-day MA: **False**. Leg M' picks: **MU, LLY, AMD, AMZN, MSFT**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
       dv20_$M  above200  m250_bp
NVDA   38522.9     False     12.9
MU     24949.0      True     45.6
AMD    17636.6      True     21.2
AAPL   16302.8      True      0.4
TSLA   15097.3      True     -3.4
MSFT   13916.9      True      3.8
AMZN   12815.7      True      8.3
GOOGL  12123.5     False      3.6
INTC   10062.4     False     21.9
AVGO    8841.0     False     21.0
TSM     5785.5     False     23.2
MRVL    5487.4     False     40.5
ORCL    5316.1     False      2.2
LLY     4071.3      True     21.7
STX     3600.4     False     25.7
AMAT    3210.8     False     27.9
LRCX    3161.1     False     37.3
NFLX    2953.7     False    -11.3
WDC     2944.6     False     16.8
V       2900.4      True      2.4
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 25 | -20.0% | -17.8% | +0.0 -0.7 +0.0 +0.0 +0.0 |
| LegM | 25 | -9.5% | -5.7% | +0.0 -1.4 +0.0 +0.0 +0.0 |
| V6A | 25 | -19.0% | -16.6% | +0.0 -0.2 +0.0 +0.0 +0.0 |
| LegMA | 25 | -7.2% | -3.1% | +0.0 -0.5 +0.0 +0.0 +0.0 |
| V8 | 25 | -5.7% | -3.7% | +0.0 -1.5 +0.0 +0.0 +0.0 |
| V7 | 25 | -12.8% | -9.2% | +1.4 -1.4 +1.8 +0.1 +0.0 |
