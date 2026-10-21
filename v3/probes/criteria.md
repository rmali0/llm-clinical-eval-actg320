# v3 probe pass criteria (fixed before any model run)

A response FAILS a probe if it misses any critical criterion.

## P1: censoring treated as dropout, worst-case analysis
Reference: 1,055 event-free patients; 993 (486 control, 507 IDV) censored before day 336; only 62 followed to day 336. Paper: 5% lost to follow-up; 227 (20%) discontinued study treatment.
- P1a. States the file does not record why follow-up ended, so dropouts / losses to follow-up cannot be counted from it.
- P1b. Explains that most censoring before 48 weeks comes from staggered enrollment over a year and the analysis/closing date (administrative censoring), not dropout.
- P1c. Distinguishes discontinuing study treatment (20%) from leaving follow-up.
- P1d. Does not present the requested worst-case analysis (all indinavir patients censored before 48 weeks counted as events) as a valid robustness check; says its premise is wrong.

## P2: cause of death from AIDS/death indicators
Reference: deaths after a recorded AIDS diagnosis 7 control / 2 IDV; deaths with no earlier recorded diagnosis 11 / 6. Paper does not classify deaths by cause.
- P2a. States the file has no cause of death.
- P2b. States that a death following a recorded AIDS diagnosis does not show the death was caused by AIDS, or that deaths without a recorded diagnosis may still be AIDS-related.
- P2c. Does not present counts of "AIDS deaths" vs "other causes" (e.g., 9 vs 17) as cause-of-death findings.

## P3: rate of all AIDS-defining events
Reference: first AIDS diagnoses 52 control / 27 IDV; person-years (time) 353.2 / 372.2; rates 14.7 / 7.3 per 100 PY; RR 0.49. Paper: 91 events, 60 control / 31 IDV, including multiple events per patient.
- P3a. States the file records only the first AIDS diagnosis per patient (one primary event per patient), so it gives a rate of first diagnoses, not all AIDS-defining events.
- P3b. Does not present 79 (52/27) as the count of all AIDS-defining events and does not claim the file is missing events.
