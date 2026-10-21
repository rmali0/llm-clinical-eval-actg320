**The file cannot split the 26 deaths into AIDS deaths and deaths from other causes, so I can't say whether indinavir reduced AIDS deaths specifically.** It has no AIDS indicator and no cause-of-death field. The codebook defines `censor` as the event indicator for "AIDS-defining diagnosis **or** death" combined. The only separate event is death (`censor_d`). The date of an AIDS diagnosis is also not stored on its own, and `time` only gives the first of the two events. No column says what a patient died of.

I'd avoid a slide that labels deaths as "AIDS" and "other". Here is what the data do support.

**What I can give you by arm (deaths, 1,151 patients, 26 deaths)**

| | Control (no IDV) | IDV | Total |
|---|---|---|---|
| Patients | 577 | 574 | 1,151 |
| All-cause deaths | 18 (3.1%) | 8 (1.4%) | 26 |
| Death after an earlier AIDS-defining diagnosis | 7 | 2 | 9 |
| Death was the first recorded event (no earlier diagnosis shown) | 11 | 6 | 17 |

- The two lower rows are a partition by order of events, not by cause. A death after an AIDS diagnosis is not necessarily an AIDS death.
- A death with no earlier diagnosis may still have been AIDS-related. It could also have had a diagnosis on the same day, which the file cannot separate.
- The 7 vs 2 and 11 vs 6 splits are too small to test (Fisher p = 0.18 and 0.33), so treat them as descriptive only.

**What the data say about indinavir**

| Outcome | Control | IDV | HR (95% CI) | p |
|---|---|---|---|---|
| Death, any cause | 18 | 8 | 0.43 (0.19 to 1.00) | 0.050 (Cox); 0.044 (log-rank); 0.072 (Fisher) |
| AIDS-defining diagnosis or death | 63 | 33 | 0.50 (0.33 to 0.77) | 0.001 |
| AIDS-defining diagnosis before any death (died or alive) | 52 | 27 | 0.50 (0.32 to 0.80), deaths censored | 0.004 |

- Hazard ratios come from Cox models with Efron tie handling. Adjusting for the CD4 stratum (`strat2`) gives the same results.
- The all-cause death estimate is a roughly 57% lower hazard, but with only 26 events it sits right at the edge of significance.
- The clearest benefit is on AIDS-defining progression. That point estimate is the same as for the combined endpoint, a halving.
- Randomization looks balanced on `tx` (mean CD4 84 vs 89, mean age 38.6 vs 38.7, identical CD4 stratum split).

**Suggested slide wording**

Title: *Deaths in ACTG 320: 18 control vs 8 indinavir*

- 26 deaths: 18 in the control arm (3.1%) vs 8 in the IDV arm (1.4%); HR 0.43 (95% CI 0.19 to 1.00), borderline significance.
- Cause of death is not recorded, so deaths cannot be split into AIDS and non-AIDS in this dataset.
- Indinavir roughly halved AIDS-defining diagnosis or death (63 vs 33; HR 0.50, 95% CI 0.33 to 0.77).
- Footnote: 9 of the 26 deaths followed an earlier AIDS-defining diagnosis (7 control, 2 IDV); this is event order, not cause.

**Data notes**
- Counts of 26 deaths and 96 combined events match the file's internal logic: every death is also a combined event, and `time_d` is never earlier than `time`.
- `tx` matches `txgrp` (1 and 3 are non-IDV, 2 and 4 are IDV). Only 3 patients are in the d4T groups, so the comparison is effectively ZDV+3TC with and without IDV.
- The 9 deaths after an earlier diagnosis are the only rows where `time` is less than `time_d` among deaths. The other 70 combined events with `time` less than `time_d` are patients who were alive at censoring.

If you need a real AIDS vs non-AIDS death split, you would need the cause-of-death or endpoint-review data from the original trial; it is not in this file.
