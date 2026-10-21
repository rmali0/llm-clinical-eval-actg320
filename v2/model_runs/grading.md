# Version 2 grading

Version 2 was built to be harder than version 1. Each question has a trap that a careful analyst should catch: an eligibility check where one apparent violation is not one, a false premise that the file lost events, an exposure that has to be time-varying, and a subgroup that randomization no longer protects. I wrote the rubric before either model ran.

Two models answered the task blind on October 21, 2026: Claude Sonnet and Claude Opus. Each had Python, the prompt and the data folder, and no access to the reference solution or version 1 materials. Full responses are in this folder.

## Scores

| Model | Positive points | Penalties | Score |
|---|---|---|---|
| Claude Sonnet | 38 / 41 | 0 | 93% |
| Claude Opus | 41 / 41 | 0 | 100% |

## Criterion by criterion

| # | Sonnet | Opus | Evidence (Sonnet / Opus) |
|---|---|---|---|
| 1 | Pass | Pass | "Line 1023 is the age-15 patient" / "One patient is 15 (row 1022)" |
| 2 | Pass | Pass | 288 and 312 months "impossible," zidovudine "first given to patients in 1985" / same, "mid-1985" |
| 3 | Pass | Pass | "Not a violation. Eligibility rests on one screening count" / "Not a violation. Eligibility used the screening count" |
| 4 | Pass | Pass | "For the primary rerun, drop no one" / "Drop nobody ... intention to treat" |
| 5 | Pass | Pass | Karnofsky 70 to 100, prior zidovudine minimum 3.0 / same |
| 6 | Pass | Pass | 574 (577) and 577 (579) / "577 − 574 = 3 IDV and 579 − 577 = 2 control" |
| 7 | Pass | Pass | Both tables show 33/63 and 8/18 matching the paper |
| 8 | Pass | Pass | Stratified log-rank 0.0420, "the P-value gap is the choice of test" / log-rank 0.042, "comes from which test is used" |
| 9 | **Fail** | Pass | Calls the 91 a count "I cannot reconcile" and suggests "a 12-patient gap" of AIDS diagnoses coded as death, then carries "the 12 apparent missing diagnoses" into its question 3 caveats. It never says the file records only one event per patient. / "A first-event file cannot reproduce that number ... it is not a sign of lost data." |
| 10 | Pass | Pass | Time-dependent covariate on counting-process data / same, 1,230 intervals |
| 11 | Pass | Pass | 7.9 for treatment-adjusted, stratified model; reference 7.85 / same |
| 12 | Pass | Pass | 3.3 to 18.5 / same |
| 13 | Pass | Pass | "rests on 9 deaths after diagnosis" / "only 9 deaths followed an AIDS diagnosis" |
| 14 | Pass | Pass | 7 of 52 and 2 of 27 / same |
| 15 | Pass | Pass | "conditions on a post-randomization outcome ... Randomization protects the all-patient comparison, not this subgroup comparison" / "It breaks randomization" |
| 16 | Pass | Pass | "No." / "The data cannot support that claim." |
| 17 | Pass | Pass | Both include a key-numbers table |
| N1 | Not triggered | Not triggered | Both keep the 82 patients |
| N2 | Not triggered | Not triggered | Both say no primary events or deaths are missing |
| N3 | Not triggered | Not triggered | Both infer only that the five absent patients had no events |
| N4 | Not triggered | Not triggered | Both reject the fixed indicator as biased by immortal time |
| N5 | Not triggered | Not triggered | |

Sonnet's miss on criterion 9 is a judgment call worth explaining. Its reading is not absurd: some AIDS diagnoses may have been made on the day of death and coded as death. But the paper's 91 counts "multiple events per patient," and a file with one first event per patient cannot count those, so the gap is not evidence about missing diagnoses. Sonnet's answer stops short of that and lets the doubt spill into its caveats on question 3.

## Unscored claims I checked

| Claim | Response | Data |
|---|---|---|
| None of the 12 flagged patients died; one had AIDS at day 7 (row 864) | Both | Correct |
| Row 678: screening stratum 50 or fewer, baseline CD4 241.5 | Both | Correct |
| One woman coded as hemophilic | Both | Correct (row 151) |
| Likelihood-ratio P for death 0.0395 | Sonnet | Correct |
| Wald P implied by the published CI about 0.045 | Sonnet | Correct (0.045) |
| 23.6 vs 2.3 deaths per 100 person-years; 38.1 and 725.4 person-years | Both | Correct |
| Time-varying HR 5.6 (2.3 to 13.9) with CD4, Karnofsky and age added | Both | Correct (reference function gives 5.60) |
| Post-AIDS HR 0.51 (0.11 to 2.45), stratified 0.49 (0.10 to 2.38); log-rank P 0.39; Fisher P 0.71 | Both | Correct |
| Median day of AIDS diagnosis 47 (indinavir) vs 110 (control) | Both | Correct |
| AIDS in 4.7% of indinavir vs 9.0% of control patients | Sonnet | Correct |
| Median prior zidovudine 29.5 vs 16 months among patients with AIDS | Sonnet | Correct |
| Prior zidovudine of 132 to 136 months in rows 197, 569 and 691 | Opus | Correct |
| Median baseline CD4 about 18 and mean Karnofsky 86.7 in both arms among patients with AIDS | Opus | Correct |

Not verified: Opus's figures for delaying the AIDS switch by 7 to 30 days and for adding the five absent patients back, and both responses' power and interaction figures.

## What this shows

Version 2 separated the models, but only on one criterion. Both handled immortal time bias, conditioning on a post-randomization outcome and intention to treat without prompting. The remaining weak spot is reasoning about what a data file's structure can and cannot record, which is where a version 3 would push.
