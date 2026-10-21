# Version 2 reference answer

Values come from `v2/solution/reference_analysis.py`. Published figures are from Hammer et al., N Engl J Med 1997;337:725-33.

| Item | File | Paper |
|---|---|---|
| Patients, indinavir / control | 574 / 577 | 577 / 579 |
| AIDS or death, indinavir / control | 33 / 63 | 33 / 63 |
| Deaths, indinavir / control | 8 / 18 | 8 / 18 |
| Death P-value | Wald 0.048; stratified log-rank 0.042 | 0.04 (log-rank) |
| AIDS-defining events | 79 patients with AIDS as first event | 91 events, including multiple events per patient |
| Patients to drop from efficacy analysis | None (intention to treat) | All randomized patients analyzed |
| HR for death after AIDS, time-varying | 10.7 (4.6 to 24.8) unadjusted; 7.9 (3.3 to 18.5) adjusted for treatment, stratified | Not reported |
| Deaths after AIDS, control / indinavir | 7 of 52 / 2 of 27 | Not reported |

**1. Eligibility and impossible values.** One patient is 15, below the minimum age (four are 16, which may or may not meet "more than 16" depending on exact age). Three patients have 288 or 312 months of prior zidovudine, meaning treatment began in 1972 or 1973. That is about a decade before HIV was identified and before zidovudine was first used for it in 1985, so the values are impossible. Four more values (150 to 172 months) are also longer than zidovudine had been available. The 82 patients with a baseline CD4 above 200 do not breach eligibility: eligibility and stratification used the screening count, and the baseline count in the file is the mean of two later measurements. Minimum prior zidovudine (3 months) and minimum Karnofsky score (70) meet the criteria. Drop nobody from the efficacy analysis. The trial was analyzed by intention to treat on all randomized patients; set the impossible prior zidovudine values to missing if that variable is used as a covariate.

**2. Reconciliation.** The file holds 3 fewer indinavir and 2 fewer control patients than the paper, but its primary events (33 and 63) and deaths (8 and 18) match the paper exactly, so no events were lost. Why the five patients are absent cannot be determined from the file. The P-value gap is the test: the stratified Cox Wald test gives 0.048, while the stratified log-rank test gives 0.042, which the paper reports as 0.04. The 91 AIDS-defining events cannot be checked against the file, because the file holds one row per patient with only the first endpoint event, so it cannot count repeat diagnoses.

**3. AIDS and the hazard of death.** AIDS has to enter the model as a time-dependent covariate that switches on at diagnosis, because patients must survive until diagnosis. A fixed "ever developed AIDS" flag counts that survival time as exposed and biases the estimate down (6.3 unadjusted, 4.2 adjusted). The time-varying hazard ratio is 10.7 (95% CI 4.6 to 24.8) unadjusted, or 7.9 (3.3 to 18.5) adjusted for treatment and stratified by `strat2`. The crude rate ratio, 23.6 vs 2.3 deaths per 100 person-years, agrees. The estimate rests on 9 deaths after diagnosis.

**4. Survival after AIDS by arm.** Among patients who developed AIDS, 7 of 52 control and 2 of 27 indinavir patients died (Cox HR from diagnosis 0.51, 95% CI 0.11 to 2.45, P = 0.40). This comparison cannot show a benefit. Developing AIDS happened after randomization and was itself affected by treatment, so the two groups of patients with AIDS are no longer comparable by design. With 9 deaths, the estimate is also compatible with large benefit or harm. The supportable claim is the randomized one: fewer deaths overall on indinavir (8 vs 18, HR 0.43).
