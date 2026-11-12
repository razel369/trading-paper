# Paper trading — signal for the close of 2026-11-11
_Generated 2026-11-11 21:29 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- cash

**LegM** — Leg M' 100% (blind-passed)
- cash

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- cash

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- cash

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- cash

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- trend SPY: exposure +16% of capital (long via UPRO / short via SPXU; divide by fund leverage) — hold
- trend QQQ: exposure +10% of capital (long via TQQQ / short via SQQQ; divide by fund leverage) — hold
- trend IWM: exposure +14% of capital (long via TNA / short via TZA; divide by fund leverage) — hold
- trend TLT: exposure -20% of capital (long via TMF / short via TMV; divide by fund leverage) — hold
- trend IEF: exposure -38% of capital (long via TYD / short via TYO; divide by fund leverage) — hold
- trend GLD: exposure +9% of capital (long via UGL / short via GLL; divide by fund leverage) — hold
- trend SLV: exposure +5% of capital (long via AGQ / short via ZSL; divide by fund leverage) — hold
- trend DBC: exposure +12% of capital (long via DBC / short via -; divide by fund leverage) — hold
- trend USO: exposure +5% of capital (long via UCO / short via SCO; divide by fund leverage) — hold
- trend UUP: exposure +45% of capital (long via UUP / short via UDN; divide by fund leverage) — hold
- trend EFA: exposure +17% of capital (long via EFA / short via EFZ; divide by fund leverage) — hold
- trend EEM: exposure +9% of capital (long via EDC / short via EDZ; divide by fund leverage) — hold
- trend VNQ: exposure +15% of capital (long via DRN / short via DRV; divide by fund leverage) — hold
- trend FXE: exposure -48% of capital (long via ULE / short via EUO; divide by fund leverage) — hold
- trend FXY: exposure -28% of capital (long via YCL / short via YCS; divide by fund leverage) — hold
- trend XLE: exposure +9% of capital (long via ERX / short via ERY; divide by fund leverage) — hold

SOXX above 200-day MA: **False**. Leg M' picks: **none (cash)**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
Empty DataFrame
Columns: [dv20_$M, above200, m250_bp]
Index: []
```

## Performance since start (model = synthetic leverage as in backtests; real = actual funds)

| strategy | nights | model | real | last 5 real |
|---|---|---|---|---|
| V6 | 23 | -20.0% | -17.8% | +0.0 +9.7 +0.0 -0.7 +0.0 |
| LegM | 23 | -9.5% | -5.7% | +0.0 +0.0 +0.0 -1.4 +0.0 |
| V6A | 23 | -19.0% | -16.6% | +0.0 +9.7 +0.0 -0.2 +0.0 |
| LegMA | 23 | -7.2% | -3.1% | +0.0 +0.0 +0.0 -0.5 +0.0 |
| V8 | 23 | -5.7% | -3.7% | +0.0 +0.0 +0.0 -1.5 +0.0 |
| V7 | 22 | -14.4% | -10.9% | +0.3 -4.2 +1.1 +1.4 -1.4 |
