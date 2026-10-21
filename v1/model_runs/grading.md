# Version 1 grading

Two models answered the task blind: Claude Sonnet and Claude Opus, each with Python code execution, the prompt and the data folder, and no access to the reference solution. Runs were made on October 21, 2026. Full responses are in this folder.

## Scores

| Model | Positive points | Penalties | Score |
|---|---|---|---|
| Claude Sonnet | 47 / 47 | 0 | 100% |
| Claude Opus | 47 / 47 | 0 | 100% |

## Criterion by criterion

| # | Sonnet | Opus | Evidence (Sonnet / Opus) |
|---|---|---|---|
| 1 | Pass | Pass | "first AIDS-defining diagnosis or death (`time`, `censor`)" / "The primary endpoint is an AIDS-defining diagnosis or death" |
| 2 | Pass | Pass | Cox on `tx`, stratified by `strat2` / same |
| 3 | Pass | Pass | HR 0.50 / HR 0.50 |
| 4 | Pass | Pass | 0.33 to 0.76 / 0.33 to 0.76 |
| 5 | Pass | Pass | p = 0.0012 / p = 0.001 |
| 6 | Pass | Pass | Baseline CD4 is "a derived baseline value, whereas the stratum is what was randomized" / baseline CD4 "does not line up with the screening strata" |
| 7 | Pass | Pass | Kaplan-Meier at day 336 / same |
| 8 | Pass | Pass | 13.1% / 13.1% |
| 9 | Pass | Pass | 6.8% / 6.8% |
| 10 | Pass | Pass | 6.3 points / 6.3 points |
| 11 | Pass | Pass | NNT 16 / NNT 16 |
| 12 | Pass | Pass | 18 vs 8 / 18 vs 8 |
| 13 | Pass | Pass | HR 0.43 (0.19 to 0.99) / same |
| 14 | Pass | Pass | "How much weight it can carry: not much," 26 events / "should carry limited weight," 26 deaths |
| 15 | Pass | Pass | 0.49 and 0.51 / 0.50 and 0.51 |
| 16 | Pass | Pass | Interaction p = 0.95 / p = 0.95 |
| 17 | Pass | Pass | "Not supported," wider interval from fewer events / "The data do not support this" |
| 18 | Pass | Pass | 17 deaths first / 17 |
| 19 | Pass | Pass | 79 AIDS-defining diagnoses first / 79 |
| 20 | Pass | Pass | Both state the `time_d` equals `time` rule and the same-day limitation |
| 21 | Pass | Pass | Both include a table |
| N1 | Not triggered | Not triggered | |
| N2 | Not triggered | Not triggered | Both use `tx`; both note the three d4T patients |
| N3 | Not triggered | Not triggered | |
| N4 | Not triggered | Not triggered | |
| N5 | Not triggered | Not triggered | |

## Unscored claims I checked

Both responses went beyond the rubric. I checked the extra figures I could verify from the data (`extra_checks` in `v1/solution/reference_values.json`):

| Claim | Response | Data |
|---|---|---|
| 28 control and 34 IDV patients under observation at day 336 | Both | Correct |
| Last primary event on day 298 (control) and 288 (IDV) | Sonnet; Opus gives 298 | Correct |
| About 725 person-years of follow-up | Sonnet | Correct (725.4) |
| Baseline CD4 up to 242 in the "50 or fewer" stratum, down to 12 in "above 50" | Opus | Correct (241.5 and 12) |
| Three patients in the d4T groups | Opus | Correct |
| Implausible prior zidovudine values of 312, 312 and 288 months | Sonnet | Correct |

Not verified: Opus's figures for one added death in the IDV arm and its reverse Kaplan-Meier median follow-up, and both responses' statements that the trial stopped early, which come from outside the data file.

Only Sonnet flagged the implausible `priorzdv` values. The prompt did not ask for a data quality check, so this is not scored.
