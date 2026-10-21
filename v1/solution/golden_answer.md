# Reference answer

All values come from `v1/solution/reference_analysis.py` (Cox models use Efron ties; 48 weeks = day 336).

| Estimate | Control (n = 577) | IDV regimen (n = 574) | Effect (95% CI) | p |
|---|---|---|---|---|
| AIDS-defining diagnosis or death, events | 63 | 33 | HR 0.50 (0.33 to 0.76), Cox stratified by `strat2` | 0.001 |
| Probability of the primary endpoint by 48 weeks (Kaplan-Meier) | 13.1% | 6.8% | Difference 6.3 points; NNT 16 | |
| Deaths | 18 | 8 | HR 0.43 (0.19 to 0.99), stratified | 0.048 |
| Screening CD4 of 50 or fewer (67 events) | | | HR 0.49 (0.30 to 0.82) | 0.006 |
| Screening CD4 above 50 (29 events) | | | HR 0.51 (0.24 to 1.10) | 0.085 |
| Treatment by stratum interaction | | | Ratio of HRs 1.03 (0.41 to 2.58) | 0.95 |
| First event: AIDS-defining diagnosis / death | 52 / 11 | 27 / 6 | 79 / 17 in total | |

**1. Primary endpoint.** The primary endpoint is the composite of an AIDS-defining diagnosis or death (`time`, `censor`). A Cox model with `tx` as the only covariate, stratified by the screening CD4 stratum (`strat2`), gives HR 0.50 (95% CI 0.33 to 0.76), p = 0.001. The stratified log-rank test agrees (p = 0.001). The stratum has to come from `strat2`, not from a cut of the `cd4` column: `cd4` is a baseline value averaged over several measurements, and 88 patients fall on the other side of 50 from their screening stratum.

**2. Probability by 48 weeks.** Kaplan-Meier estimates at day 336 are 13.1% in the control arm and 6.8% in the IDV arm, an absolute difference of 6.3 percentage points and an NNT of about 16 over 48 weeks. The last primary event occurred on day 298, so these values are carried forward through a thin tail of follow-up.

**3. Death alone.** There were 26 deaths (18 vs 8). The stratified Cox HR is 0.43 (0.19 to 0.99), p = 0.048. This result points the same way as the primary endpoint but carries limited weight: it rests on 26 events, the upper confidence bound sits almost at 1, and without stratification p is 0.050. It supports the primary result rather than proving a survival benefit on its own.

**4. The colleague's subgroup claim.** Not supported. The stratum-specific HRs are nearly identical (0.49 and 0.51). The interval for screening CD4 above 50 crosses 1 because that stratum had only 29 events, not because the effect was smaller. The treatment-by-stratum interaction test shows no difference (ratio of HRs 1.03, p = 0.95). The absolute benefit is larger in the low-CD4 stratum because its baseline risk is higher.

**5. First events.** Of the 96 primary events, 79 were AIDS-defining diagnoses and 17 were deaths, counting a death as the first event when `time_d` equals `time`. The other 9 deaths came after an AIDS diagnosis. The file cannot separate a diagnosis and death on the same day, so such a pair counts as a death under this rule.
