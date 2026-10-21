# Version 2 scoring rubric

Each criterion is scored pass or fail from the response text alone. Reference values are in `v2/solution/reference_values.json`. I wrote this rubric before running either model.

**Score** = (points from passed positive criteria minus points from triggered negative criteria) / 41.

## Question 1: eligibility and data check

| # | Criterion | Points |
|---|---|---|
| 1 | Flags the patient aged 15 as below the minimum age. | 2 |
| 2 | Flags the prior zidovudine values of 288 and 312 months (3 patients) as impossible, with a reason tied to when zidovudine was first used for HIV or when HIV was identified. | 3 |
| 3 | States that a baseline CD4 above 200 (82 patients) is not an eligibility breach, because eligibility used the screening count and the baseline count is a separate measurement. | 3 |
| 4 | Recommends keeping all randomized patients, including flagged ones, in the efficacy analysis (intention to treat). | 3 |
| 5 | Reports that the minimum prior zidovudine (3 months) and the minimum Karnofsky score (70) meet the criteria. | 1 |

## Question 2: reconciling the file with the paper

| # | Criterion | Points |
|---|---|---|
| 6 | States the file has 574 indinavir and 577 control patients, 3 and 2 fewer than the paper. | 2 |
| 7 | States that primary events (33 and 63) and deaths (8 and 18) in the file match the paper exactly. | 3 |
| 8 | Reproduces a death P-value of about 0.04 with a log-rank test (0.042 stratified or 0.044 unstratified) and attributes the gap from 0.048 to the test used. | 3 |
| 9 | Explains that the 91 AIDS-defining events cannot be checked against the file because it records only one endpoint event per patient, so the file's count of AIDS diagnoses is not evidence of lost events. | 3 |

## Question 3: AIDS diagnosis and the hazard of death

| # | Criterion | Points |
|---|---|---|
| 10 | Models AIDS as a time-dependent covariate that switches on at the date of diagnosis (start-stop or counting-process data). | 4 |
| 11 | The reported time-varying hazard ratio matches the reference for the stated adjustment set within 10% (10.7 unadjusted; 7.9 adjusted for treatment and stratified by `strat2`; 9.9 adjusted for treatment without stratification; other sets recomputed with the reference function). | 2 |
| 12 | Reports a 95% CI for that hazard ratio. | 1 |
| 13 | Notes that the estimate rests on few deaths after an AIDS diagnosis (9). | 1 |

## Question 4: survival after AIDS by arm

| # | Criterion | Points |
|---|---|---|
| 14 | Reports deaths after an AIDS diagnosis by arm: 7 of 52 control and 2 of 27 indinavir. | 2 |
| 15 | States that restricting to patients who developed AIDS compares groups formed after randomization, so the comparison is no longer protected by randomization. | 4 |
| 16 | Concludes the data cannot show that indinavir improved survival after an AIDS diagnosis. | 3 |

## Format

| # | Criterion | Points |
|---|---|---|
| 17 | Includes a table of the key numbers. | 1 |

## Negative criteria

| # | Criterion | Points |
|---|---|---|
| N1 | Recommends treating patients with a baseline CD4 above 200 as ineligible or excluding them. | −3 |
| N2 | Concludes that the file is missing primary events or deaths. | −3 |
| N3 | States a specific reason for the five absent patients as fact. | −2 |
| N4 | Answers question 3 with a hazard ratio from a fixed "ever developed AIDS" indicator measured from randomization. | −3 |
| N5 | Claims the data show that indinavir improved survival after an AIDS diagnosis. | −3 |
