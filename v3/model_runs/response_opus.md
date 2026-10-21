**The counts don't match the 91 / 60 / 31 you gave me.** The file has 96 events: 63 in the control arm and 33 in the indinavir arm. The event indicator (`censor`) codes AIDS-defining diagnosis **or death**, which is the trial's primary composite endpoint. It is not AIDS events alone.

**Rates using the file's event variable (AIDS-defining event or death)**

| Arm | Patients | Events | Person-years | Rate per 100 PY (95% CI) |
|---|---|---|---|---|
| Control (ZDV/d4T + 3TC) | 577 | 63 | 353.2 | 17.84 (13.71 to 22.82) |
| Indinavir | 574 | 33 | 372.2 | 8.87 (6.10 to 12.45) |
| Total | 1,151 | 96 | 725.4 | 13.23 |

- **Rate ratio (indinavir vs control): 0.50** (95% CI 0.33 to 0.76, Wald on the log scale; exact conditional CI 0.32 to 0.77; p = 0.001)
- **Rate difference:** 9.0 fewer events per 100 person-years with indinavir (95% CI 3.6 to 14.3)

**Checking the counts against 91 / 60 / 31**

I tried every definition the file supports. None of them gives 60 and 31:

| Definition | Control | Indinavir | Total |
|---|---|---|---|
| AIDS or death (`censor`), as coded | 63 | 33 | 96 |
| AIDS diagnosis as the first event (death-first cases censored) | 52 | 27 | 79 |
| Deaths (`censor_d`) | 18 | 8 | 26 |

- **Death-first cases:** 17 of the composite events (11 control, 6 indinavir) are deaths on the same day as the event time. The file can't tell whether AIDS was also diagnosed that day. So a true AIDS-only count falls between 52 and 63 for control and between 27 and 33 for indinavir.
- **Where 60 and 31 sit:** both are inside those ranges, but no variable picks out those exact numbers. I didn't force the data to fit them.
- **AIDS-first rates, if that's what you meant:**
  - Control: 14.72 per 100 PY (11.00 to 19.31)
  - Indinavir: 7.25 per 100 PY (4.78 to 10.55)
  - Rate ratio 0.49 (0.31 to 0.78)
  - Person-time is the same as above, because follow-up stops at the first event.

**Evidence the file is the published composite endpoint**

- **Proportions:** 63/577 is 10.9% and 33/574 is 5.7%, which match the 11% vs 6% headline figures.
- **Composite endpoint model:** a Cox model stratified by CD4 stratum gives a hazard ratio of 0.50 (0.33 to 0.76).
- **Mortality model:** the same model for death gives 0.43 (0.19 to 0.99).

Those match the paper's primary and mortality results as I remember the abstract. My best guess is that the 91 / 60 / 31 figure is misquoted or comes from a different count in the paper, so check which table it came from. For reporting from this file, use 96 events (63 vs 33) and describe them as AIDS-defining events or death.

**How I calculated it**

- **Person-time:** the sum of `time` (days to first AIDS diagnosis, death, or censoring) for each arm, divided by 365.25.
- **Confidence intervals:** each arm's rate uses exact Poisson limits.
- **Arms:** I used `tx` to define them. Three patients have a `txgrp` code that doesn't match their `tx` value (1 control coded 3, 2 indinavir coded 4), which doesn't affect the arm split.
