## ACTG 320, part 2: data checks, reconciliation, and the AIDS-to-death question

Row numbers below count data rows in actg320.csv, excluding the header. All Cox models are stratified by `strat2` (the randomization CD4 stratum) and use Efron ties unless I say otherwise.

### 1. Eligibility and impossible values

| Criterion / check | What the file shows | Verdict |
|---|---|---|
| Age > 16 | One patient is 15 (row 1022, IDV, censored at day 298). Four are 16 (rows 266, 317, 864, 931). | Age 15 breaks the criterion. Age 16 in completed years still counts as "more than 16" unless the patient enrolled on their birthday, so check dates of birth. |
| CD4 ≤ 200 | 82 patients have `cd4` > 200 (maximum 392). | Not a violation. Eligibility used the screening count, and `cd4` is a baseline value derived from several measurements. 88 patients fall on the "wrong" side of 50 for their `strat2`, which is ordinary CD4 variability. Row 678 is worth a query: its screening stratum is ≤ 50 but its derived CD4 is 241.5. |
| Prior ZDV ≥ 3 months | Minimum is 3. Everyone meets it. | Met. |
| Prior ZDV, plausibility | Values of 312 (rows 200, 825), 288 (row 1143), 172 (row 231), 160 (row 509), 156 (row 675, a 20-year-old) and 150 (row 980) months. | **Impossible.** Zidovudine was first given to patients in mid-1985. By the last randomization (January 1997) the longest possible exposure is about 139 months. Rows 197, 691 and 569 (132 to 136 months) are possible only for the earliest trial participants, so query them too. |
| Karnofsky ≥ 70 | All values are 70 to 100. | Met. |
| Internal consistency | No `time` > `time_d`. No death without `censor` = 1. Every censored record has `time` = `time_d`. No duplicates. | Clean. |
| Other | 20 patients have CD4 = 0, which is possible in advanced HIV. One woman has hemophilia (row 151), which is rare but possible. | Query only. |

**Drop nobody.** ACTG 320 was analyzed by intention to treat, and the published numbers include all 1,156 randomized patients. Removing patients after randomization because of eligibility findings or bad baseline values breaks that comparison. None of the 12 flagged patients died, and only one had an endpoint (row 864, AIDS at day 7). The right steps are:
- Send the flagged values back to the data manager.
- Set the impossible `priorzdv` values to missing for any covariate-adjusted model.
- Leave the treatment comparison alone.

As a check, dropping all 12 flagged patients moves the composite HR from 0.499 to 0.508 and the death HR from 0.432 to 0.430.

### 2. Reconciling the file with the paper

**The file did not lose any events.** Endpoint counts match the paper exactly by arm:
- AIDS or death: 33 on IDV and 63 on control.
- Deaths: 8 and 18.

The 5 missing patients (577 − 574 = 3 IDV and 579 − 577 = 2 control) all had no events and were censored.

The P = 0.048 versus 0.04 gap comes from which test is used, not from missing data:

| Death analysis | HR (95% CI) | P |
|---|---|---|
| Stratified Cox, Wald test (your model) | 0.432 (0.188 to 0.993) | 0.048 |
| Stratified Cox, likelihood ratio test | same | 0.040 |
| Stratified log-rank (score) test | same | 0.042 |
| Published | 0.43 (0.19 to 0.99) | 0.04 |

- The published P matches the stratified log-rank test.
- The published confidence interval is the Wald interval, and a Wald interval with an upper limit of 0.99 implies P ≈ 0.047. Your 0.048 is therefore consistent with the paper's own CI.
- Adding the 5 missing censored patients back in any stratum, at any time from day 1 to day 364, keeps the Wald P between 0.046 and 0.049 and the log-rank P between 0.040 and 0.043.

The composite endpoint reproduces exactly: HR 0.499 (0.328 to 0.761), Wald P = 0.0012 and log-rank P = 0.0010, against the published 0.50 (0.33 to 0.76), P = 0.001.

**About the 91 AIDS-defining events.** A file with one row per patient and first events only splits the 96 endpoints into:
- 79 patients whose first event was AIDS (27 IDV, 52 control);
- 17 deaths with no earlier AIDS diagnosis.

If 91 were a count of patients, only 5 deaths would have come without AIDS, which disagrees with the 17 in the file. So 91 is most likely a count of diagnoses, since some patients had more than one, or it includes AIDS diagnosed on the day of death. A first-event file cannot reproduce that number. Because the endpoint counts match by arm, it is not a sign of lost data.

### 3. Hazard of death after an AIDS-defining diagnosis

**For the slide: HR 7.9 (95% CI 3.3 to 18.5), P < 0.001.**

How I modeled it:
- **Model:** a Cox model for death with AIDS as a time-varying covariate, stratified by CD4 stratum and adjusted for treatment arm. Each of the 79 AIDS patients contributes AIDS-free time from entry to diagnosis and AIDS time from diagnosis to death or censoring, giving 1,230 intervals. The covariate switches on from the day after diagnosis.
- **Crude rates:** 17 deaths in 725 person-years before AIDS (2.3 per 100 person-years) and 9 deaths in 38 person-years after AIDS (23.6 per 100 person-years). The crude rate ratio is 10.1 (exact CI 4.0 to 23.9).
- **Robustness:**
  - A profile-likelihood CI gives 3.2 to 18.1.
  - Delaying the switch by 7 to 30 days gives 7.0 to 7.4.
  - Also adjusting for baseline CD4, Karnofsky and age reduces it to 5.6 (2.3 to 13.9). That model has only about 5 deaths per covariate.
- **Do not use an "ever had AIDS" baseline indicator.** It counts pre-AIDS survival time as AIDS time (immortal time bias) and gives a misleading 4.2.

Caveats for the slide footnote:
- The interval is wide because only 9 deaths followed an AIDS diagnosis.
- This is an association: the AIDS diagnosis marks disease progression and is not a cause you can intervene on.
- The 17 same-day records are counted as deaths without AIDS. If some were really AIDS diagnosed at death, the true ratio is higher.

### 4. Survival after AIDS by arm

**The data cannot support that claim.** The raw numbers among patients who developed AIDS point the right way but prove nothing:

| | IDV | Control |
|---|---|---|
| Developed AIDS | 27 | 52 |
| Died after AIDS | 2 (7.4%) | 7 (13.5%) |
| Post-AIDS death rate | 14.7 per 100 person-years | 28.5 per 100 person-years |
| Median days from entry to AIDS | 47 | 110 |

- **Effect estimate:** HR 0.49 (0.10 to 2.38), P = 0.38, from a Cox model on time since diagnosis. Fisher's exact test gives P = 0.71. The AIDS-by-arm interaction in the time-dependent model is 0.80 (0.12 to 5.15).
- **It breaks randomization.** AIDS is a post-randomization outcome that indinavir itself affects, since it roughly halved the AIDS rate. The IDV patients who still developed AIDS are a selected group. Their diagnoses came much earlier (median 47 vs 110 days), which suggests disease already under way at entry or non-response. Measured baseline factors look similar (median CD4 18 in both arms, mean Karnofsky 86.7 in both), but adherence, resistance and viral response were not measured.
- **It has almost no power.** With 9 deaths, the CI runs from a 90% reduction to a more than twofold increase.

What the data do support is the randomized mortality result, HR 0.43 (0.19 to 0.99). Descriptively, the IDV arm had fewer deaths both without prior AIDS (6 vs 11) and after AIDS (2 vs 7). If you want to show the post-AIDS comparison, label it exploratory and non-randomized.

### Key numbers

| Item | File (n = 1,151) | Published (n = 1,156) |
|---|---|---|
| Patients, IDV / control | 574 / 577 | 577 / 579 |
| AIDS or death, IDV / control | 33 / 63 | 33 / 63 |
| HR, AIDS or death | 0.50 (0.33 to 0.76), P = 0.001 | 0.50 (0.33 to 0.76), P = 0.001 |
| Deaths, IDV / control | 8 / 18 | 8 / 18 |
| HR, death | 0.43 (0.19 to 0.99); Wald P = 0.048, log-rank P = 0.042 | 0.43 (0.19 to 0.99), P = 0.04 |
| AIDS as first event / death as first event | 79 / 17 patients | 91 AIDS-defining events (a count of diagnoses, not patients) |
| Eligibility and value flags | 1 age 15, 4 age 16 (check dates of birth), 7 impossible prior-ZDV values | Drop none (intention to treat) |
| HR of death after AIDS diagnosis | 7.9 (3.3 to 18.5); 5.6 (2.3 to 13.9) with full adjustment | Not reported |
| Deaths after AIDS, IDV / control | 2/27 vs 7/52; HR 0.49 (0.10 to 2.38), P = 0.38 | Not a valid randomized comparison |
