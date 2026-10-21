# ACTG 320: Key Estimates from actg320.csv

The file has 1,151 randomized patients: 577 on the control regimen and 574 on the indinavir (IDV) regimen. The primary endpoint is an AIDS-defining diagnosis or death. 48 weeks is taken as day 336.

| Estimate | Control | IDV regimen | Effect (95% CI) | p |
|---|---|---|---|---|
| Primary endpoint events / patients | 63 / 577 | 33 / 574 | HR 0.50 (0.33 to 0.76) | 0.001 |
| Probability of primary endpoint by 48 weeks (Kaplan-Meier) | 13.1% (10.3 to 16.6) | 6.8% (4.8 to 9.5) | Absolute difference 6.3 points (2.4 to 10.3); NNT 16 (10 to 42) | |
| Deaths | 18 | 8 | HR 0.43 (0.19 to 0.99) | 0.048 |
| CD4 of 50 or fewer at screening: events / patients | 44 / 220 | 23 / 219 | HR 0.50 (0.30 to 0.82) | 0.006 |
| CD4 above 50 at screening: events / patients | 19 / 357 | 10 / 355 | HR 0.51 (0.24 to 1.10) | 0.085 |
| Treatment by stratum interaction | | | Ratio of HRs 1.03 (0.41 to 2.58) | 0.95 |
| First primary events: AIDS-defining / death | 52 / 11 | 27 / 6 | 79 / 17 in total | |

**1. Effect on the primary endpoint**

I fitted a Cox proportional hazards model on `time` and `censor`. Its only covariate was the treatment indicator `tx` (1 = IDV regimen). The model was stratified on `strat2`, the screening CD4 stratum, so each stratum gets its own baseline hazard. That matches the stratified randomization. Ties used the Efron method, and all patients were analyzed in their assigned arm.

- **Result:** HR 0.50 (95% CI 0.33 to 0.76), Wald p = 0.0012. The stratified log-rank test agrees (chi-square 10.9, p = 0.001). The IDV regimen roughly halved the hazard of AIDS or death.
- **Stratum variable:** I used `strat2` rather than the `cd4` column. Baseline CD4 is derived from several measurements and does not line up with the screening strata. Baseline CD4 runs up to 242 in the "50 or fewer" stratum and down to 12 in the "above 50" stratum.
- **Robustness:**
  - Dropping the stratification gives HR 0.50 (0.33 to 0.77).
  - Adding baseline CD4, age, Karnofsky score, prior zidovudine, sex, IV drug use and hemophilia gives HR 0.51 (0.34 to 0.78).
  - A test of treatment by log time found no evidence against proportional hazards (p = 0.26).
- **Treatment groups:** `tx` is the comparison. Three patients coded to the d4T-based groups are included under their `tx` value.

**2. Probability of the primary endpoint by 48 weeks**

The Kaplan-Meier estimates by day 336 are 13.1% in the control arm and 6.8% in the IDV arm.

- **Absolute difference:** 6.3 percentage points (2.4 to 10.3).
- **Number needed to treat:** about 16 (10 to 42). Treating 16 patients with the IDV regimen for 48 weeks prevents one AIDS diagnosis or death.
- **Caveat on the tail:** follow-up was short.
  - Median follow-up was 38 weeks (reverse Kaplan-Meier), and no one was followed past day 364.
  - Only 62 patients (28 control, 34 IDV) were still under observation at day 336.
  - The last primary event was on day 298, so the 48-week values are the curves carried flat from about week 43.

**3. Death alone**

The same stratified Cox model on `time_d` and `censor_d` gives HR 0.43 (0.19 to 0.99), Wald p = 0.048 (likelihood-ratio p = 0.040). This result should carry limited weight:

- **Few events:** there were only 26 deaths (18 vs. 8). The interval runs from an 81% reduction to a 1% reduction.
- **Fragile p-value:** one more death in the IDV arm would give HR 0.49 (0.22 to 1.08), p = 0.08.
- **Not independent:** death is a secondary endpoint and also part of the primary composite. It is not separate confirmation of the main result.
- **Early stop:** the follow-up pattern reflects a trial stopped early for benefit, and early stopping tends to overstate effect sizes.

It is fair to call the mortality result consistent with and supportive of the primary finding. It is not a standalone demonstration of a survival benefit.

**4. Did indinavir help only patients with CD4 of 50 or fewer?**

The data do not support this.

- **Same relative effect:** the stratum hazard ratios are almost identical, 0.50 and 0.51. The interaction test gives p = 0.95, with a ratio of HRs of 1.03 (0.41 to 2.58).
- **Why the interval crosses 1:** the above-50 stratum had 29 events against 67 in the other stratum, so its estimate is less precise. The effect itself was not smaller.
- **Continuous CD4:** using baseline CD4 on a log scale gives the same answer (interaction p = 0.73).
- **The right test:** a non-significant subgroup result is not evidence of no effect. The question is answered by the interaction test.
- **What does differ is absolute benefit,** because baseline risk differs:

| CD4 at screening | 48-week risk, control | 48-week risk, IDV | Absolute difference | NNT |
|---|---|---|---|---|
| 50 or fewer | 23.5% | 11.8% | 11.7 points | about 9 |
| Above 50 | 6.4% | 3.6% | 2.7 points | about 37 |

The interaction test has low power, so a moderate difference cannot be excluded either. Still, nothing in these data points to a difference.

**5. Composition of the primary events**

Of the 96 primary endpoint events, 79 were AIDS-defining diagnoses and 17 were deaths.

- **Counting rule:** an event counts as a death only when `censor_d` = 1 and `time_d` equals `time`. The other 9 of the 26 deaths came after an earlier AIDS diagnosis (`time_d` later than `time`), so those patients count as AIDS events.
- **Common error:** counting every death would give 26 deaths and 70 AIDS events, which is wrong.
- **By arm:** control had 52 AIDS events and 11 deaths; the IDV arm had 27 and 6.
- **Limitation:** an AIDS diagnosis made on the day of death would be counted as a death, because the file cannot tell the two apart.
