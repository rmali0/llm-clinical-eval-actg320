# ACTG 320 teaching case: summary of estimates

## Setup
- **Data:** 1,151 patients (577 control, 574 indinavir), with no missing values. `tx` agrees with `txgrp` for every patient.
- **Primary endpoint:** first AIDS-defining diagnosis or death (`time`, `censor`). There were 96 events: 63 in the control arm and 33 in the indinavir arm.
- **Follow-up:** the maximum is 364 days and the median is 257 days. This is about 725 person-years, so the crude event rates are 17.8 vs 8.9 per 100 person-years.
- **Randomization stratum:** I used `strat2`, the screening CD4 stratum, not baseline `cd4`. The two disagree for 88 patients (34 in stratum 0 have baseline CD4 above 50, and 54 in stratum 1 have 50 or less). The CD4 count is a derived baseline value, whereas the stratum is what was randomized.

## Key estimates

| Question | Result | 95% CI | p |
|---|---|---|---|
| 1. Primary endpoint, HR (IDV vs control), Cox stratified by `strat2` | 0.50 | 0.33 to 0.76 | 0.0012 |
| 2. 48-week risk, control (Kaplan-Meier) | 13.1% | 10.2% to 16.6% | |
| 2. 48-week risk, IDV | 6.8% | 4.8% to 9.5% | |
| 2. Absolute risk difference | 6.3 points | 2.4 to 10.3 | 0.0016 |
| 2. Number needed to treat (48 weeks) | 16 | 10 to 42 | |
| 3. Death alone, HR (stratified Cox) | 0.43 | 0.19 to 0.99 | 0.048 |
| 4. HR, CD4 50 or fewer (439 pts, 67 events) | 0.49 | 0.30 to 0.82 | 0.006 |
| 4. HR, CD4 above 50 (712 pts, 29 events) | 0.51 | 0.24 to 1.10 | 0.085 |
| 4. Ratio of HRs (treatment by stratum interaction) | 1.03 | 0.41 to 2.58 | 0.95 |
| 5. First events: deaths / AIDS-defining diagnoses | 17 / 79 (of 96) | | |

## 1. Effect on the primary endpoint
- **Model:** Cox proportional hazards on `time` and `censor`, with treatment (`tx`, 1 = IDV) as the only covariate. It is stratified by the screening CD4 stratum (`strat2`), which mirrors the stratified randomization. Ties use the Efron method.
- **Result:** HR 0.50 (95% CI 0.33 to 0.76), Wald p = 0.0012. The stratified score test gives p = 0.00098 and the likelihood-ratio test gives p = 0.0009. Indinavir about halved the hazard of AIDS or death.
- **Sensitivity checks:** the result barely moves under other specifications.
  - Unstratified: HR 0.50 (0.33 to 0.77).
  - Adjusted for baseline CD4, age, Karnofsky score, sex, hemophilia and prior zidovudine months, still stratified: HR 0.52 (0.34 to 0.79).
  - Splitting follow-up at day 90, the HR is 0.71 before day 90 and 0.35 after. The difference is not significant (p = 0.11), so the proportional hazards assumption looks acceptable. The early effect is weaker, though.

## 2. Probability of the endpoint by 48 weeks (day 336)
- **Method:** Kaplan-Meier estimates by arm, with log-log confidence intervals. The risk difference uses Greenwood standard errors.
- **Control:** 13.1% (95% CI 10.2% to 16.6%).
- **IDV:** 6.8% (95% CI 4.8% to 9.5%).
- **Difference:** 6.3 percentage points (2.4 to 10.3). The NNT is 1/0.063, about 16, with a 95% CI of 10 to 42.
- **Caveat on the tail:** the last primary event was at day 298 in the control arm and day 288 in the IDV arm. Only 28 control and 34 IDV patients were still under observation at day 336. The estimates are therefore carried forward from the last event time and rest on a thin tail. Standardizing the risks to the stratum mix gives about the same values (12.9% and 6.7%).
- **Why the NNT is time-specific:** the HR is similar in both CD4 strata, but baseline risk differs a lot between them. The NNT at 48 weeks is about 9 for CD4 50 or fewer (23.5% vs 11.8%) and about 37 for CD4 above 50 (6.4% vs 3.6%). These stratum figures are descriptive only.

## 3. Death alone
- **Counts:** 26 deaths in total, 18 in the control arm and 8 in the IDV arm, using `time_d` and `censor_d`.
- **Result:** the stratified Cox HR is 0.43 (95% CI 0.19 to 0.99), Wald p = 0.048. It points the same way as the composite, with a similar magnitude.
- **How much weight it can carry: not much.**
  - It rests on 26 events, so the interval runs from an 81% reduction to essentially no effect.
  - Whether it clears p < 0.05 depends on the test:

    | Analysis | p |
    |---|---|
    | Likelihood-ratio | 0.040 |
    | Score | 0.042 |
    | Unstratified Wald | 0.050 (upper CI 1.000) |
    | Adjusted for baseline covariates | 0.052 |
    | Fisher exact test on the 18 vs 8 counts | 0.072 |

  - It is a secondary component analysis with no multiplicity adjustment.
  - Deaths account for a minority of the composite events.
  - From the published trial report, not this file: the trial was stopped early at an interim review. This is the setting where small-event results tend to be overstated.
- **Suggested wording for the session:** the mortality result is consistent with the composite and suggestive of benefit. It is not conclusive on its own. The 48-week Kaplan-Meier mortality was 4.2% vs 1.6%.

## 4. "Indinavir only helped patients with CD4 of 50 or fewer"
**Not supported.**
- The stratum-specific hazard ratios are nearly identical: 0.49 vs 0.51.
- The interval in the CD4-above-50 group crosses 1 because it has only 29 events, against 67 in the other group. A wider interval from fewer events is not evidence of no effect.
- The correct test is the treatment-by-stratum interaction: ratio of HRs 1.03 (0.41 to 2.58), p = 0.95. A continuous treatment-by-baseline-CD4 interaction also shows nothing (p = 0.96).
- **Limit on this conclusion:** the interaction interval is wide, so the data cannot rule out moderate differences between strata. They also give no reason to believe one exists.
- **Where the colleague has a point:** on the absolute scale the benefit is larger in the low-CD4 group, because those patients start at a higher risk (see the stratum NNTs under question 2).

## 5. Composition of the 96 primary events (first event per patient)
- **Deaths as the first event:** 17 (11 control, 6 IDV).
- **AIDS-defining diagnoses as the first event:** 79 (52 control, 27 IDV).
- **Why the counts differ from the 26 total deaths:** 9 of the 79 patients with an AIDS-defining diagnosis first died later in follow-up. Those deaths count in question 3 but not here.
- **Classification rule:** a patient counts as a death-first event when `time_d` equals `time`. The file cannot separate a death from a diagnosis on the same day, so any same-day pair would be classed as death.

## Data notes
- `priorzdv` has implausible values for a 1997 trial (two patients at 312 months and one at 288, which exceeds the time zidovudine had been available). It is used only in the adjusted sensitivity model, and the result is the same without it (HR 0.51, 0.33 to 0.77).
- The primary analysis uses no baseline covariates beyond the stratum.
