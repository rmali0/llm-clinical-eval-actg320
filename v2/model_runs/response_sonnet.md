**Short answers**
1. Drop nobody from the primary analysis. The file has a few bad values, but none changes the efficacy result, and dropping patients after randomization departs from intention to treat. A sensitivity list is given below.
2. The file lost no events. It reproduces every published count. Your P = 0.048 is a Wald test, and the published 0.04 matches a likelihood-ratio or log-rank test on the same model.
3. HR for death after an AIDS diagnosis is 7.9 (95% CI 3.3 to 18.5), from a Cox model with AIDS as a time-dependent covariate.
4. No. Only 9 deaths follow a diagnosis, and comparing arms among patients who developed AIDS conditions on a post-randomization outcome.

---

## 1. Eligibility and impossible values

I checked the file for missing values, duplicates, out-of-range codes, `tx` against `txgrp`, and event logic. There are no missing values or duplicate rows. Every code is in range, `tx` matches `txgrp`, and `time_d` is never less than `time`. Every death is also a composite event. The codebook's own range checks pass.

Two of the report's criteria cannot fail in this file. Karnofsky is 70 to 100 for all patients, and prior zidovudine is 3 months or more for all patients (minimum 3.0).

| Check | Finding | Verdict |
|---|---|---|
| Age over 16 | 5 patients aged 16 or under (age 15: 1; age 16: 4). File lines 267, 318, 865, 932, 1023 (header is line 1). Line 1023 is the age-15 patient. | Only age 15 is clearly ineligible. Age is in whole years, so a 16-year-old can still be "more than 16". One of the five had an AIDS event (day 7). None died. |
| CD4 of 200 or less | 82 patients have file `cd4` above 200 (max 392; 21 are at 250 or above; 6 are above 300). | Not a violation. Eligibility rests on one screening count within 60 days. The file's `cd4` is derived from multiple measurements, and the screening value is not in the file. `strat2` disagrees with `cd4` for 88 patients (34 with `strat2`=0 and cd4 above 50; 54 with `strat2`=1 and cd4 of 50 or less), which fits that derivation. |
| CD4 vs `strat2` | File line 679 has `strat2`=0 (screening CD4 of 50 or less) but cd4 = 241.5. | The one contradiction large enough to query at source. Keep the patient. |
| Prior zidovudine | 7 patients have 150 to 312 months (150, 156, 160, 172, 288, 312, 312). File lines 201, 232, 510, 676, 826, 981, 1144. | Impossible for 1996 to 1997 enrollment. Zidovudine was first given to patients in 1985, so about 11 years is the ceiling. The next highest value is 136. They still satisfy the 3-month minimum, and none had an event. |
| Sex and hemophilia | 1 woman coded as hemophilic (line 152). | Rare. Possible miscoding, but not an eligibility variable. |

**Who to drop.** For the primary rerun, drop no one. The paper's analysis was on everyone randomized, and none of these problems is related to outcome. The prior zidovudine errors are in a covariate that is not in the efficacy model, so set those 7 values to missing rather than dropping the patients. If you want a sensitivity analysis, drop the 5 aged 16 or under, and optionally the 7 with impossible prior zidovudine. I would not drop the 82 with cd4 above 200. That removes one IDV death, leaves 25 deaths, no longer reproduces the published counts, and moves the HR to 0.38.

Stratified Cox (by `strat2`), IDV vs control, by exclusion:

| Population | n | Death HR (95% CI) | Wald P | AIDS or death HR (95% CI) | Wald P |
|---|---|---|---|---|---|
| All | 1151 | 0.432 (0.188, 0.993) | 0.048 | 0.499 (0.328, 0.761) | 0.0012 |
| Drop age 16 or under | 1146 | 0.433 (0.188, 0.995) | 0.049 | 0.510 (0.335, 0.779) | 0.0018 |
| Drop prior ZDV 150 months or more | 1144 | 0.430 (0.187, 0.988) | 0.047 | 0.497 (0.326, 0.757) | 0.0011 |
| Drop both, plus line 679 | 1138 | 0.429 (0.186, 0.986) | 0.046 | 0.506 (0.331, 0.772) | 0.0016 |

The conclusions do not change under any of these exclusions.

## 2. Reconciling the file with the published results

**No events are missing.**

| | IDV | Control | Total |
|---|---|---|---|
| Patients, file (published) | 574 (577) | 577 (579) | 1151 (1156) |
| AIDS or death, file (published) | 33 (33) | 63 (63) | 96 (96) |
| Deaths, file (published) | 8 (8) | 18 (18) | 26 (26) |

The 5 missing patients (3 IDV, 2 control) therefore had no events. Adding 5 event-free patients back, with follow-up anywhere from 1 to 364 days, changes the Wald P only from 0.0482 to between 0.0479 and 0.0482.

**The P-value gap is the choice of test.** All of these use the same data and the `strat2`-stratified model for death:

| Test | P |
|---|---|
| Wald (your 0.048) | 0.0482 |
| Likelihood ratio | 0.0395 |
| Score | 0.0419 |
| Stratified log-rank | 0.0420 |
| Unstratified log-rank | 0.0438 |

Efron and Breslow tie handling give the same answer (0.0482 vs 0.0483). My HR of 0.432 (0.188 to 0.993) matches the published 0.43 (0.19 to 0.99). A Wald P computed from the published CI is 0.045, so the paper's 0.04 almost certainly came from a likelihood-ratio or log-rank test, with the CI from the Wald interval. To match the paper, report the likelihood-ratio or log-rank P (0.04). Either way the result is fragile: 26 deaths, and the CI upper limit is 0.993.

The composite endpoint also reproduces. HR is 0.499 (0.328 to 0.761), Wald P 0.0012, likelihood-ratio P 0.0009, stratified log-rank P 0.0010. The paper reports 0.50 (0.33 to 0.76), P = 0.001.

**One count I cannot reconcile is the 91 AIDS-defining events.** The file has 79 patients with an AIDS diagnosis recorded before death or censoring: 70 who stayed alive through follow-up and 9 who later died. A further 17 died with no earlier diagnosis. That gives 79 + 17 = 96 first events. If the 91 means patients, then 91 + 26 − 96 = 21 patients had both an AIDS diagnosis and a death, but the file shows only 9. The 12-patient gap is plausibly deaths with an AIDS-defining event at or near death that the file codes as death only. I cannot confirm this from the file, because there is no separate AIDS date. If the 91 counts events rather than patients, there is no conflict. This does not touch the efficacy results, but it matters for questions 3 and 4.

## 3. Hazard ratio for death after an AIDS diagnosis

**Headline for the slide: HR 7.9 (95% CI 3.3 to 18.5).**

**Model.** Cox model with days since enrollment as the time scale and death (`time_d`, `censor_d`) as the event. AIDS diagnosis is a time-dependent covariate. It is 0 until the diagnosis day (`time`, for patients with `censor`=1 and `time_d` > `time`) and 1 afterward. The model includes `tx`, is stratified by `strat2`, and uses Efron ties. It is fitted on counting-process (start, stop) data.

Raw rates behind the model:
- 79 patients were diagnosed.
- After diagnosis there were 9 deaths in 38.1 person-years, or 23.6 per 100 person-years.
- Before diagnosis or without diagnosis there were 17 deaths in 725.4 person-years, or 2.3 per 100 person-years.

| Specification | HR for AIDS (95% CI) |
|---|---|
| Time-dependent AIDS, unadjusted | 10.7 (4.6, 24.8) |
| + `tx` | 9.9 (4.2, 23.1) |
| + `tx`, stratified by `strat2` (reported) | 7.9 (3.3, 18.5) |
| Same, Breslow ties | 7.8 (3.3, 18.4) |
| + `tx`, `strat2`, cd4, age, Karnofsky | 5.6 (2.3, 13.9) |
| Fixed "ever had AIDS" flag (do not use) | 4.2 (1.8, 9.7) |

The fixed baseline flag is wrong because of immortal time. Patients must survive long enough to be diagnosed, so their pre-diagnosis person-time is wrongly counted as exposed, and the HR is biased low.

**Caveats for the slide.**
- The interval is wide because it rests on 9 deaths after diagnosis.
- Across reasonable adjustments the estimate ranges from 5.6 to 10.7, and every interval excludes 1.
- The diagnosis is not randomized, so this is an association.
- If the 12 apparent missing diagnoses (question 2) are deaths with concurrent AIDS, the file's HR is for "diagnosed earlier and then died", and those deaths sit in the reference group.

## 4. Can the data show indinavir improved survival after an AIDS diagnosis?

**No.** There are two separate problems.

**Too few events.** Among the 79 patients with a diagnosis (52 control, 27 IDV):

| | Control | IDV |
|---|---|---|
| Died after diagnosis | 7 of 52 (13%) | 2 of 27 (7%) |
| Rate per 100 person-years | 28.5 | 14.7 |

- Cox model with the clock starting at diagnosis: HR 0.51 (0.11 to 2.45), P = 0.40. Stratified by `strat2`: 0.49 (0.10 to 2.38).
- Log-rank P = 0.39. Fisher exact P = 0.71.
- With 9 events, the standard error of the log HR is about 0.70. Only an HR below about 0.14 would be detectable with 80% power.

The point estimate leans toward benefit, but the data are compatible with a large benefit or with harm.

**Biased comparison.** Having AIDS is an outcome of treatment. IDV roughly halved diagnoses (4.7% of IDV patients vs 9.0% of control patients), so the two groups of AIDS patients are no longer comparable, even though they were randomized. The data show signs of this:
- Median prior zidovudine is 19 vs 22 months across all randomized patients, but 29.5 (control) vs 16 (IDV) months among those who developed AIDS.
- Median diagnosis day is 47 for IDV vs 110 for control.

Randomization protects the all-patient comparison, not this subgroup comparison.

**What you can show.** The randomized comparison is overall mortality: 8 vs 18 deaths, HR 0.43. The deaths split as follows:

| | IDV | Control |
|---|---|---|
| Deaths with no earlier recorded diagnosis | 6 | 11 |
| Deaths after a diagnosis | 2 | 7 |

In a model with a separate IDV effect before and after diagnosis, the IDV HR is 0.52 (0.19 to 1.40) before diagnosis and 0.41 (0.09 to 2.00) after. The ratio of the two is 0.80 (0.12 to 5.15). The data cannot tell whether the survival benefit comes from delaying AIDS or from improving survival after it. A defensible slide line is: "Indinavir reduced mortality overall (8 vs 18 deaths, HR 0.43)".

---

## Key numbers

| Item | Value |
|---|---|
| Patients in file / randomized | 1151 / 1156 (5 missing: 3 IDV, 2 control) |
| AIDS or death events, IDV / control | 33 / 63 (matches published) |
| Deaths, IDV / control | 8 / 18 (matches published) |
| Eligibility problems | 5 aged 16 or under (1 aged 15); 7 prior zidovudine of 150 months or more; 82 with cd4 above 200 (not testable); 1 `strat2`/cd4 contradiction (line 679) |
| Patients to drop for primary analysis | None |
| Death HR, stratified Cox | 0.432 (0.188, 0.993) |
| Death P, Wald / likelihood ratio / stratified log-rank | 0.048 / 0.040 / 0.042 |
| Composite HR, stratified Cox | 0.499 (0.328, 0.761); P 0.001 |
| AIDS diagnoses in file vs report | 79 patients vs 91 reported |
| HR for death after AIDS (time-dependent, stratified, adjusted for `tx`) | 7.9 (3.3, 18.5); range across specifications 5.6 to 10.7 |
| Deaths after diagnosis, control / IDV | 7 of 52 / 2 of 27; HR 0.51 (0.11, 2.45); P 0.39 |
| Conclusion on question 4 | Not supportable (9 events, post-randomization selection) |
