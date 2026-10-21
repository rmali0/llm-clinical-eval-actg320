**Short answer:** The file can't reproduce 91 / 60 / 31. Its event flag (`censor`) counts an AIDS-defining event **or death**, and that gives 96 events: 63 in the control arm and 33 in the indinavir arm. On that endpoint the indinavir rate is half the control rate (rate ratio 0.50). Counting AIDS events only, the most the file can confirm is 52 vs 27, and the rate ratio is about the same (0.49).

**Rates per 100 person-years**

Person-years are days of follow-up divided by 365.25. Follow-up stops at the first event or at censoring.

| Endpoint | Arm | Events | Person-years | Rate per 100 PY (95% CI) |
|---|---|---|---|---|
| AIDS or death (`censor`) | Control (n=577) | 63 | 353.2 | 17.8 (13.7 to 22.8) |
| | Indinavir (n=574) | 33 | 372.2 | 8.9 (6.1 to 12.5) |
| AIDS only (deaths with no earlier AIDS event removed) | Control | 52 | 353.2 | 14.7 (11.0 to 19.3) |
| | Indinavir | 27 | 372.2 | 7.3 (4.8 to 10.6) |

**Rate ratio, indinavir vs control**
- AIDS or death: **0.50** (95% CI 0.33 to 0.76), p = 0.001
- AIDS only: **0.49** (95% CI 0.31 to 0.78), p = 0.003

The arm rates use exact Poisson CIs and the ratios use log-scale Wald CIs. Exact conditional CIs for the ratios are almost the same: 0.32 to 0.77 and 0.30 to 0.80.

Person-time is the same under both definitions because `time` already stops at whichever comes first: AIDS, death or censoring. In the AIDS-only version, a death with no earlier AIDS event counts as censored on that day.

**Count check**

- The file has no AIDS-only flag. `censor` marks AIDS or death, and `censor_d` marks death.
- There are 26 deaths (18 control, 8 indinavir):
  - 9 came after an earlier AIDS event (`time` < `time_d`).
  - 17 (11 control, 6 indinavir) fall on the same day as the first event. Each of these is either a death with no AIDS diagnosis or an AIDS diagnosis made on the day of death, and the file can't tell which.
- So the true AIDS-only count is between 79 (52/27, if all 17 were deaths without AIDS) and 96 (63/33).
- 91 (60/31) falls inside that range. It would fit if 8 of the 11 control cases and 4 of the 6 indinavir cases were AIDS diagnoses on the day of death. That is possible, but nothing in the file can confirm it.
- The file does match the trial's primary endpoint of AIDS or death:
  - It gives 63/577 = 10.9% vs 33/574 = 5.7%, and a Cox hazard ratio of 0.50 (0.33 to 0.77). The published abstract reports 11% vs 6% and a hazard ratio of 0.50 (0.33 to 0.76).
  - Deaths alone (18 vs 8) give a hazard ratio of 0.43, which also matches the paper.
  - So the gap most likely comes from how the paper defines its 91, not from missing records. Check which table the 91 comes from and whether it includes deaths.

If you use the paper's 60 and 31 with the file's person-time, the rates are 17.0 (13.0 to 21.9) vs 8.3 (5.7 to 11.8) per 100 PY, with a rate ratio of 0.49 (0.32 to 0.76).

**Bottom line:** Whichever event definition you use, indinavir roughly halves the event rate (rate ratio 0.49 to 0.50). I'd report the 63 vs 33 figures, since that's the analysis the file directly supports, and label the endpoint as "AIDS-defining event or death" rather than AIDS alone.
