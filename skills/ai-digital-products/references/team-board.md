# TEAM-BOARD.md: how the team talks

One file, 04 Creator Pipeline\TEAM-BOARD.md. Every agent reads it at the start of a run and updates it at the end. Luis owns it and tidies it in each stand-up (moves done tasks to the log, keeps it short).

## Rules
- Write only in your own rows and messages; edit another agent's task only when you are Luis.
- Messages are one line: date, from → to, the ask. The receiver replies under it or closes it.
- Anything for Advaith goes under Needs Advaith, numbered, with exactly what will happen if he says yes.
- Keep the board under about 80 lines. Luis moves finished items to the Log as one line each and deletes log lines older than 30 days.

## Template (copy on first run)
```
# TEAM-BOARD (updated <date> by <agent>)

## Needs Advaith (approvals queue)
1. [Snippy] Send batch 2026-11-12-parenting: 10 emails today from advaith.resetlab@gmail.com, schedule and 3 samples in 02-snippy/outbox.csv rows 1, 25, 50
2. [Benji] 2 replies to @creator_a and @creator_b, drafts in partners/*/conversation-log.md

## Tasks
| ID | Owner | Task | Status | Depends on | Due |
|---|---|---|---|---|---|
| T1 | Whisky | Run 2026-11-12, 50 creators, seed parenting | done | | |
| T2 | Snippy | Send batch day 1 of 5 | waiting approval | T1 | 11-12 |
| T3 | Ted | GLP-1 for @creator_a: research batch 2 of 4 | in progress | brief | 11-15 |
| T4 | Mike | Build lesson 3 of 6 | in progress | T3 | 11-16 |
| T5 | Peter | Fix hero headline on iPhone (Luis feedback) | open | | 11-13 |

## Messages
- 11-12 Ted → Benji: ask @creator_a if her audience is mostly post-partum; changes chapter 2
- 11-12 Luis → Peter: hero headline wraps to 3 lines on iPhone 13; cut to 2

## Decisions
- 11-10 Run size stays 50 until the inbox is 2 weeks old (Luis)

## Log
- 11-11 Whisky: run 2026-11-11 done, 37 passed (budget used)
```
