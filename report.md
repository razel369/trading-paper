# Paper trading — signal for the close of 2026-10-13
_Generated 2026-10-13 20:35 New York time. Research only, not investment advice._

## Tonight's orders (buy MOC at the close, sell overnight legs MOO at the next open)

**V6** — 50% SOXL + 50% Leg M' (blind-passed)
- 50% SOXL (3x SOXX) — overnight

**LegM** — Leg M' 100% (blind-passed)
- cash

**V6A** — V6, Leg M' picks only if m250 > 10 bp (round 13, forward test)
- 50% SOXL (3x SOXX) — overnight

**LegMA** — Leg M' 100%, picks only if m250 > 10 bp (round 13, forward test)
- cash

**V8** — 50%: best 2 of 8 liquid 3x funds by m250 + 50% LegMA (round 15, forward test)
- cash

**V7** — Leg M', trend sleeve when idle (withdrawn, comparison)
- trend SPY: exposure +19% of capital (long via UPRO / short via SPXU; divide by fund leverage) — hold
- trend QQQ: exposure +12% of capital (long via TQQQ / short via SQQQ; divide by fund leverage) — hold
- trend IWM: exposure +16% of capital (long via TNA / short via TZA; divide by fund leverage) — hold
- trend TLT: exposure -21% of capital (long via TMF / short via TMV; divide by fund leverage) — hold
- trend IEF: exposure -41% of capital (long via TYD / short via TYO; divide by fund leverage) — hold
- trend GLD: exposure +9% of capital (long via UGL / short via GLL; divide by fund leverage) — hold
- trend SLV: exposure +6% of capital (long via AGQ / short via ZSL; divide by fund leverage) — hold
- trend DBC: exposure +10% of capital (long via DBC / short via -; divide by fund leverage) — hold
- trend USO: exposure +4% of capital (long via UCO / short via SCO; divide by fund leverage) — hold
- trend UUP: exposure +41% of capital (long via UUP / short via UDN; divide by fund leverage) — hold
- trend EFA: exposure +17% of capital (long via EFA / short via EFZ; divide by fund leverage) — hold
- trend EEM: exposure +9% of capital (long via EDC / short via EDZ; divide by fund leverage) — hold
- trend VNQ: exposure +18% of capital (long via DRN / short via DRV; divide by fund leverage) — hold
- trend FXE: exposure -46% of capital (long via ULE / short via EUO; divide by fund leverage) — hold
- trend FXY: exposure -21% of capital (long via YCL / short via YCS; divide by fund leverage) — hold
- trend XLE: exposure +10% of capital (long via ERX / short via ERY; divide by fund leverage) — hold

SOXX above 200-day MA: **True**. Leg M' picks: **none (cash)**

### Leg M' ranking (top-20 by 20-day dollar volume)

```
Empty DataFrame
Columns: [dv20_$M, above200, m250_bp]
Index: []
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
