**Short answer**

This file can't tell you how many patients dropped out of each arm, and the short follow-up isn't evidence of heavy dropout. Most of it comes from enrollment timing. The worst-case analysis as you described it can't be run in a meaningful way here, because it would turn 507 of the 574 indinavir patients into events. I ran a tipping-point analysis instead, which answers what the reviewer is really asking. The primary result holds unless at least 13 indinavir patients were lost to follow-up and every one of them had an unrecorded AIDS event or death, with no such events among lost control patients.

**1. Why the file can't count dropouts**

`censor = 0` only means no event was observed by last contact. The file has no off-study date, no reason for leaving and no treatment-discontinuation flag. A patient lost to follow-up therefore looks exactly like one who was still in the study when follow-up closed.

The data show that most of the censoring is administrative:

- **Follow-up ended on a common date.** Randomization ran for 364 days (Jan 29, 1996 to Jan 27, 1997), and follow-up times in the file run from 1 to 364 days. That pattern means everyone's follow-up ended on one calendar date, around when accrual closed. (ACTG 320 was stopped early at an interim review in early 1997.)
- **That is why so few reach 48 weeks.** Only patients randomized in about the first four weeks could have reached 336 days. Only 62 patients have 48 weeks of follow-up (28 control, 34 indinavir). That is a calendar effect, not attrition.
- **Follow-up continued after a primary event.** For the 96 patients with an AIDS event or death, follow-up for death ran a median of 151 days past that event.
- **Each patient has one last-contact date.** For all 1,055 censored patients, last contact for the primary endpoint is the same as last contact for death.
- **Median follow-up** (reverse Kaplan-Meier) is 265 days, about 38 weeks.

The 227 in the paper are patients who stopped study drugs, which is not the same as leaving follow-up. In an intention-to-treat analysis, patients who stop their assigned drugs stay in their randomized arm and keep being followed for AIDS events and death. It's worth confirming in the paper's methods that this follow-up continued. The file has no variable that identifies these patients, so the 227 can't be mapped onto anyone in it.

**2. Was censoring different between the arms?**

Randomization balances enrollment dates, so administrative censoring should look the same in both arms. If one arm had more dropout, its censoring pattern would differ. Here it doesn't.

| | Control (n = 577) | Indinavir (n = 574) |
|---|---|---|
| Events (AIDS or death) | 63 | 33 |
| Censored | 514 (89%) | 541 (94%) |
| Censored before 12 weeks | 36 | 31 |
| Censored at 12 to 24 weeks | 70 | 62 |
| Censored at 24 to 36 weeks | 124 | 128 |
| Censored at 36 to 48 weeks | 256 | 286 |
| Censored at 48 weeks or later | 28 | 34 |
| Median follow-up (reverse KM) | 263 days | 266 days |

- The indinavir arm has a higher share censored because it had fewer events (33 vs 63), not more dropout.
- Log-rank on censoring (reverse KM): p = 0.23.
- Kolmogorov-Smirnov test on censoring times: p = 0.66.
- If anything, slightly more control patients were censored in the first 24 weeks (106 vs 93).

**3. Worst-case sensitivity analysis**

The primary result reproduces: 63 events in the control arm vs 33 on indinavir. Stratified by CD4 stratum, the HR is 0.50 (95% CI 0.33 to 0.76), with a stratified log-rank p = 0.001.

*The analysis as specified.* 507 of 574 indinavir patients (88%) were censored before 336 days, almost all because they enrolled too late to reach 48 weeks. Counting all of them as events gives 540 indinavir events vs 63 and an HR of 7.7. That number reflects when patients enrolled, not what happened to dropouts, so I would not show it to the reviewer.

*The tipping-point version.* I picked k censored indinavir patients at random and counted each as an event at their censoring time. I left the control arm unchanged, refit the stratified analysis and repeated this 300 times for each k. The table shows median values.

| Hidden IDV events added | IDV events | HR | Upper 95% limit | Stratified log-rank p |
|---|---|---|---|---|
| 0 | 33 | 0.50 | 0.76 | 0.001 |
| 5 | 38 | 0.57 | 0.86 | 0.006 |
| 10 | 43 | 0.65 | 0.95 | 0.026 |
| 12 | 45 | 0.68 | 0.99 | 0.043 |
| 13 | 46 | 0.69 | 1.01 | 0.055 |
| 20 | 53 | 0.79 | 1.14 | 0.21 |
| 35 | 68 | 1.01 | 1.42 | 0.95 |

- **Which patients are picked hardly matters.** With 12 added events, every draw stayed below 0.05 (largest p was 0.047). With 13, only 2% did.
- **Hidden control events raise the threshold about one for one.** With 5, 10 or 20 hidden control events, it takes 18, 22 or 32 hidden indinavir events to lose significance.

How to read this:
- **If 12 or fewer indinavir patients were truly lost to follow-up,** the result holds under the strict worst case.
- **If more were lost,** you can't claim it survives the strict worst case. Hardly any trial with about 100 events would. The question then becomes whether that many hidden events is plausible.
- **Plausibility.** The indinavir arm's observed 48-week Kaplan-Meier event risk is 6.8% (control 13.1%). Suppose 50 indinavir patients were lost. For 13 hidden events to come from them, 26% would need an unrecorded event. That is about four times their own arm's observed risk and twice the control arm's, with no hidden events among lost control patients.

**What to tell the reviewer**

Suggested wording:

"The short follow-up comes from enrollment spread over 12 months and a common closing date, not from dropout. Follow-up times span the same 364 days as the accrual window, median follow-up is 38 weeks, and censoring patterns are the same in both arms (log-rank on censoring, p = 0.23). The 227 treatment discontinuations remain in the intention-to-treat analysis. In a tipping-point analysis, at least 13 unrecorded AIDS events or deaths among censored indinavir patients, with none among controls, would be needed to make the primary result non-significant, and about 35 to bring the hazard ratio to 1."

To settle the strict worst case, you need the number of patients lost to follow-up in each arm. That comes from the paper's patient-flow data or the off-study codes in the full ACTG dataset. If the indinavir count is 12 or fewer, you can say the result holds even under the strict worst case.

One caution: don't extend this argument to mortality. Deaths were 18 vs 8 (HR 0.43, 95% CI 0.19 to 0.99, stratified log-rank p = 0.042). A single hidden indinavir death makes that result non-significant (p = 0.07).
