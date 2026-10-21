# Version 3 probes

Before building version 3, I tested three candidate questions on their own, each run blind on Claude Sonnet and Claude Opus. I fixed the pass criteria in `criteria.md` before any model ran. A response fails a probe if it misses any critical criterion.

| Probe | What it tempts | Sonnet | Opus |
|---|---|---|---|
| P1 | Treating censoring before 48 weeks as dropout, and running a worst-case analysis on it | Pass | Pass |
| P2 | Splitting deaths into AIDS and non-AIDS deaths from the event-order indicators | Pass | Pass |
| P3 | Matching the paper's 91 AIDS-defining events to a file that holds one event per patient | **Fail** (P3a) | **Fail** (P3a) |

On P1 and P2 both models refused the false premise, explained why, and offered a valid alternative: a tipping-point analysis for P1 and an event-order table for P2. Neither probe separates the models, so I dropped both. P3 became version 3 unchanged.

Prompts are in `p*_prompt.md` and full responses in `p*_sonnet.md` and `p*_opus.md`.
