**The counts do not line up with the paper.** The file gives 96 events (63 control, 33 indinavir), not 91 (60 and 31). The rate ratio is about 0.50 either way.

**Why the counts differ**
- The `censor` flag in actg320.csv marks AIDS-defining diagnosis or death, whichever came first. The codebook says so. It is not an AIDS-only flag.
- The 96 events are 70 with no death during follow-up (45 control, 25 indinavir), 9 with AIDS followed by a later death (7, 2), and 17 whose event time equals their death time (11, 6).
- The 26 deaths in the file (18 control, 8 indinavir) are exactly the deaths-only counts, so the file looks intact.
- The 5-event gap to the paper (3 control, 2 indinavir) fits the idea that some deaths happened without a prior AIDS diagnosis. The file cannot show which of the 17 deaths those are, because it has no separate AIDS diagnosis date. It can only guarantee 79 AIDS-first events (52 control, 27 indinavir), which is a lower bound. So I cannot reproduce 91 from this file.
- Person-time is not affected by this ambiguity. A patient who died without AIDS is censored at the same day they would be counted as an event, so the denominators are the same under any definition.

**Person-time and arms**
- Follow-up runs from enrollment to first event or censoring, which is at most 364 days. Person-years are the summed `time` divided by 365.25.
- The control arm is `tx`=0 (577 patients, 353.2 person-years). The indinavir arm is `tx`=1 (574 patients, 372.2 person-years). Dividing by 365 instead changes nothing at two decimals.

**Rates per 100 person-years, with exact Poisson 95% CIs**

| Event definition | Control events | Control rate | Indinavir events | Indinavir rate | Rate ratio (95% CI) |
|---|---|---|---|---|---|
| AIDS or death, as coded in the file | 63 | 17.84 (13.71 to 22.82) | 33 | 8.87 (6.10 to 12.45) | 0.497 (0.326 to 0.757) |
| Paper's counts over this file's person-time | 60 | 16.99 | 31 | 8.33 | 0.490 (0.318 to 0.756) |
| AIDS-first events only (lower bound) | 52 | 14.72 | 27 | 7.25 | 0.493 (0.309 to 0.784) |

- For the first row, the exact conditional CI for the rate ratio is 0.316 to 0.769 (p = 0.001). The rate difference is 8.97 fewer events per 100 person-years on indinavir.
- The second row is a reconciliation, not a patient-level analysis. It pairs the paper's numerators with this file's denominators, since I cannot identify those 91 patients.
- Whatever the true AIDS-only count is, it lies between the first and third rows. Across every possible split of the 17 ambiguous patients, the rate ratio ranges from 0.41 to 0.60, and the realistic values cluster near 0.49 to 0.50.
- Cross-checks agree. A Poisson regression with a person-time offset gives the same 0.497 and CI as the first row, and a Cox model on `time` and `censor` gives a hazard ratio of 0.50.

**What to report**
- I would give the first row, labelled "AIDS-defining event or death", with rates of 17.8 and 8.9 per 100 person-years and a rate ratio of 0.50 (95% CI 0.33 to 0.76).
- Do not call it the paper's 91-event AIDS-only outcome. Only the original trial data, with separate AIDS diagnosis dates, can reproduce 60 and 31.
