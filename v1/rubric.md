# Version 1 scoring rubric

Each criterion is scored pass or fail from the response text alone. Numeric ranges allow for rounding and for reasonable tie-handling choices (Efron or Breslow). Reference values are in `v1/solution/reference_values.json`.

**Score** = (points from passed positive criteria minus points from triggered negative criteria) / 47.

## Question 1: primary endpoint

| # | Criterion | Points |
|---|---|---|
| 1 | Identifies the primary endpoint as the composite of an AIDS-defining diagnosis or death, using `time` and `censor`. | 3 |
| 2 | Fits a Cox model with `tx` as the treatment term, stratified by `strat2`. | 3 |
| 3 | Reports a hazard ratio for the primary endpoint between 0.48 and 0.52. | 3 |
| 4 | Reports a 95% CI for that hazard ratio with a lower bound between 0.31 and 0.35 and an upper bound between 0.74 and 0.78. | 2 |
| 5 | Reports a p-value for that hazard ratio between 0.0005 and 0.002. | 1 |
| 6 | States that `strat2` (CD4 at screening) is used instead of a grouping built from the baseline `cd4` column, because the two measure CD4 at different points. | 2 |

## Question 2: probability by 48 weeks

| # | Criterion | Points |
|---|---|---|
| 7 | Estimates the 48-week probability with a Kaplan-Meier (or equivalent survival) estimate at day 336. | 2 |
| 8 | Reports a 48-week probability in the control arm between 12.8% and 13.4%. | 2 |
| 9 | Reports a 48-week probability in the IDV arm between 6.5% and 7.1%. | 2 |
| 10 | Reports an absolute difference between 6.0 and 6.6 percentage points. | 2 |
| 11 | Reports a number needed to treat between 15 and 17. | 2 |

## Question 3: death alone

| # | Criterion | Points |
|---|---|---|
| 12 | Reports 18 deaths in the control arm and 8 in the IDV arm. | 2 |
| 13 | Reports a death hazard ratio between 0.41 and 0.45 with a 95% CI upper bound between 0.95 and 1.02. | 2 |
| 14 | States that the death result carries limited weight and gives a reason (few deaths, or a CI upper bound near 1). | 3 |

## Question 4: the subgroup claim

| # | Criterion | Points |
|---|---|---|
| 15 | Reports hazard ratios for both screening CD4 strata, each between 0.45 and 0.56. | 2 |
| 16 | Reports a treatment-by-stratum interaction test with p above 0.5. | 3 |
| 17 | Concludes the colleague's claim is not supported, because a CI crossing 1 in the smaller stratum is not evidence that the effect is absent there. | 3 |

## Question 5: first events

| # | Criterion | Points |
|---|---|---|
| 18 | Reports 17 deaths as the first primary event. | 3 |
| 19 | Reports 79 AIDS-defining diagnoses as the first primary event. | 3 |
| 20 | States the counting rule for first events or notes that a same-day diagnosis and death cannot be separated in the file. | 1 |

## Format

| # | Criterion | Points |
|---|---|---|
| 21 | Includes a table of the key estimates. | 1 |

## Negative criteria

| # | Criterion | Points |
|---|---|---|
| N1 | Describes the 96 primary endpoint events as AIDS diagnoses alone. | −3 |
| N2 | Uses `txgrp` (four groups) as the treatment comparison instead of `tx`. | −2 |
| N3 | Concludes that indinavir had no effect in the screening CD4 above 50 stratum. | −3 |
| N4 | Presents the death result as proof of a survival benefit with no caveat. | −2 |
| N5 | Reports 26 deaths among the first primary events. | −2 |
