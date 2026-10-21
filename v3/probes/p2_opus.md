**This file can't split the 26 deaths into AIDS deaths and deaths from other causes, because it doesn't record cause of death.** `censor` isn't an AIDS indicator. Per the codebook it marks the composite endpoint, an AIDS-defining diagnosis *or* death, so every death has `censor = 1` automatically. In the data, all 26 deaths have `censor = 1`, and no one has `censor = 0` with `censor_d = 1`.

What the two time variables can show is the **order of events**. A death has either an earlier AIDS-defining diagnosis (`time < time_d`) or no prior recorded diagnosis, meaning death was the first event (`time == time_d`).

**Deaths by arm and by what came first**

| | Control (n = 577) | IDV (n = 574) | Total |
|---|---|---|---|
| Death after an earlier AIDS-defining diagnosis | 7 | 2 | 9 |
| Death as the first recorded event | 11 | 6 | 17 |
| **All deaths** | **18 (3.1%)** | **8 (1.4%)** | **26** |

Neither row tells you the cause of death:
- A patient diagnosed with AIDS can later die of something unrelated.
- A death with no earlier recorded diagnosis can still be AIDS-related. An opportunistic illness found at or near death, or a diagnosis on the day of death, would show up as `time == time_d`.

Labelling the rows "AIDS deaths" and "non-AIDS deaths" on the slide would be wrong.

Note on arms: `txgrp` has 576 and 572 patients in groups 1 and 2, but only 1 and 2 in the d4T groups (3 and 4). Those three patients had no events. So I compared IDV against control using `tx`.

**Did indinavir reduce AIDS deaths specifically?**

This file can't answer that. Here is what it does support:

| Endpoint | Control | IDV | Hazard ratio (95% CI) | Log-rank p |
|---|---|---|---|---|
| AIDS-defining diagnosis or death (primary composite) | 63 (10.9%) | 33 (5.7%) | 0.50 (0.33 to 0.77) | 0.001 |
| Recorded AIDS-defining diagnosis | 52 (9.0%) | 27 (4.7%) | 0.50 (0.32 to 0.80) | 0.003 |
| Death from any cause | 18 (3.1%) | 8 (1.4%) | 0.44 (0.19 to 1.00) | 0.04 |
| Death after an earlier AIDS-defining diagnosis | 7 | 2 | 0.28 (0.06 to 1.35) | 0.09 |
| Death as the first recorded event | 11 | 6 | 0.53 (0.20 to 1.44) | 0.21 |

- Indinavir clearly reduced AIDS-defining events and the composite endpoint, roughly halving the hazard.
- It also reduced deaths from any cause, but only just reached significance: log-rank p = 0.04, Wald p = 0.050, and the upper CI limit is right at 1.00. That's 26 deaths in under a year of follow-up (median about 265 days).
- Both event-order rows point the same way, and neither is significant. Among those who died, the share with an earlier AIDS diagnosis was 2 of 8 on IDV and 7 of 18 on control (Fisher p = 0.67). So even this stand-in for cause shows no sign that indinavir affected one kind of death more than the other.
- Fewer IDV deaths had an earlier AIDS diagnosis partly because IDV prevented AIDS diagnoses in the first place. That's a knock-on effect of the composite result, not evidence about cause of death.

**Suggested slide framing**

- Title: "Deaths by arm, by whether an AIDS-defining event came first"
- Use the first table above.
- Footnote: "Cause of death is not recorded in this dataset. Rows show the order of events, not cause. All-cause mortality: 8 vs 18 deaths, HR 0.44 (95% CI 0.19 to 1.00)."
- Takeaway line: "Indinavir halved AIDS-defining events or death. The all-cause death reduction was only just significant, and this dataset can't say which causes of death were reduced."

To actually answer the question about AIDS deaths, you'd need the trial's adjudicated cause-of-death records, which aren't in this file.
