# Paper trading — overnight strategies

Automatic paper trading of the strategies from the research lab. Runs on GitHub Actions every US trading day,
no computer needed. Research only — not investment advice.

- **report.md** — tonight's orders for each strategy and performance since start (updated ~16:40–17:40 New York time).
- **signal_preview.md** — the same signal from intraday prices at ~15:35 New York time, in time for market-on-close orders.
- **equity.csv** — every settled night: model return (synthetic leverage, as in the backtests) and real return
  (actual 2x/3x funds; the stock itself when no 2x fund exists).
- **journal.json** — every decision and its result.

Strategies tracked: V6 (50% SOXL + 50% Leg M'), Leg M' alone, V7 (Leg M' + trend sleeve when idle; comparison).
Rules: see STRATEGIES.md in the lab. Fills assumed at the close (MOC) and the next open (MOO), cost 0.05% per round trip.
