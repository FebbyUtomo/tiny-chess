# Tiny Chess Engine (4 KB)

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/FebbyUtomo/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard)
[![reward](https://make.fun/badge/tiny-chess-01/FebbyUtomo/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A small, strong chess engine in a single Python file (`main.py`, 4,096 bytes),
written for the make.fun bounty "Build the strongest chess engine in 4 KB of
Python" (tiny-chess-01).

## What it is

- 120-square board, side-to-move always "white" (rotate on every move).
- Incremental piece-square evaluation (material + PSTs), king-capture legality
  (castling, en passant, promotion handled; move generation verified by perft).
- Alpha-beta search with iterative deepening to a fixed 150,000-node budget,
  quiescence on captures, and a best-move table for ordering.
- Deterministic: fixed node budget, no clock, no randomness.
- Standard library only, Python 3.13. Talks to the make.fun env over HTTP
  (`MAKEFUN_ENV_URL`): `/game`, `/move`, `/resign`.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

## Test it

Move generation is verified by perft (startpos + kiwipete + en-passant/pin and
promotion positions all match the known counts), and the engine finds mate in 1
in the Scholar's-mate test position. A local match harness (`match.py`, not part
of the entry) plays it against the public sunfish 4 KB engine.

## License

MIT. See `LICENSE`.
