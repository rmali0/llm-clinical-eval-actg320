**Short answer:** The file has no field that identifies dropouts, so I can't count them by arm. The worst-case analysis you specified does not support "the result holds even then." It reverses the result, and the reason is a problem with the definition, not the drug. The observed result survives only a small tipping-point scenario (up to about 11 IDV events), described below.

## What the file contains

- The file has no variable for treatment discontinuation, withdrawal or last contact. `censor = 0` only means no AIDS diagnosis or death was seen by the censoring time.
- The paper's 227 patients (20%) discontinued study treatment. That is different from being lost to follow-up. As I understand the design, patients who stopped treatment were still followed for the endpoint, so they would not be censored in this file. Please check this against the paper.
- Follow-up is capped by the calendar, not by dropout:
  - The maximum time in the file is 364 days. The randomization window you gave (January 29, 1996 to January 27, 1997) is also 364 days.
  - That fits a common closing date close to the last randomization. Anyone randomized after roughly the first month could not reach 48 weeks (336 days). The file has no dates, so I can't confirm this.
  - Only 62 patients (5.4%) have 336 days or more: 28 control and 34 IDV.
  - Nobody has an event after day 298, so all 96 events fall inside the 48-week window.

## Censoring by arm (this is not the same as dropout)

| | Control (n=577) | IDV (n=574) |
|---|---|---|
| Primary events (AIDS or death) | 63 (10.9%) | 33 (5.7%) |
| Censored before day 336 | 486 (84.2%) | 507 (88.3%) |
| Followed to day 336 or later | 28 (4.9%) | 34 (5.9%) |
| Median potential follow-up (reverse Kaplan-Meier) | 263 days | 266 days |

- **Censored before day 336:** The 4-point gap (Fisher p = 0.049) is arithmetic. Control has 30 more events, and events leave the censored group. The correct comparison is a log-rank test on the censoring times, which gives p = 0.23, so there is no evidence that censoring differs by arm.
- **Early censoring:** Only 13 patients were censored before day 28 (9 control, 4 IDV), too few to interpret.
- **How to describe the 993 patients censored before day 336:** They are "censored before 48 weeks, mostly administratively." They are not dropouts.

## Worst-case analysis as requested

I set `censor = 1` at the censoring time for every IDV patient censored before day 336. That reclassifies 507 of 574 IDV patients. The stratified Cox model uses the CD4 stratum (`strat2`) and Breslow ties.

| | Events, control | Events, IDV | Hazard ratio, IDV vs control (95% CI) | p |
|---|---|---|---|---|
| Observed | 63/577 | 33/574 | 0.50 (0.33 to 0.76) | 0.001 |
| Literal worst case | 63/577 | 540/574 (94%) | 7.71 (5.94 to 10.01) | <0.001 |

The result reverses. It would reverse in any trial with this follow-up structure, because the analysis counts the closing date as treatment failure. Showing it to the reviewer would hurt the case without telling them anything about dropout.

## A worst case that can be defended

I added events to randomly chosen IDV patients censored before day 336. I also built the least favourable choice, adding one at a time the patient who moves the hazard ratio most.

| Extra IDV events | Hazard ratio (95% CI) | p |
|---|---|---|
| 0 | 0.50 (0.33 to 0.76) | 0.001 |
| 10 | 0.65 (0.44 to 0.95) | 0.03 |
| 11 (least favourable choice) | 0.67 (0.46 to 0.98) | 0.041 |
| 12 (least favourable choice) | 0.69 (0.47 to 1.00) | 0.052 |
| 20 | 0.79 (0.55 to 1.14) | 0.21 |
| 35 | about 1.0 | about 0.9 |
| 115 (about 20% of the IDV arm) | 2.16 (1.61 to 2.90) | <0.001 |

- **Tipping point:** Significance is lost at 12 added events in the least favourable case, or 13 in a typical random draw. That is about 2% of the IDV arm.
- **What this supports:** The finding is robust if no more than about 11 IDV patients were truly lost to follow-up and all of them had an event. It is not robust to losses on the scale of the paper's 227 under an all-events assumption.
- **Applying the 227 figure:** Those are treatment discontinuations, not losses to follow-up. The figure only applies here if those patients also stopped being followed.

## What to tell the reviewer

- This file cannot measure dropout.
- The heavy censoring before 48 weeks reflects the staggered enrollment and a common closing date. Censoring is balanced between arms.
- The effect holds if no more than about 11 IDV patients were both lost to follow-up and had an event.
- To do the sensitivity analysis properly, get the discontinuation and last-contact data from the full ACTG 320 dataset or the paper's tables, count lost-to-follow-up patients by arm, and rerun the tipping-point analysis with the true IDV number.
