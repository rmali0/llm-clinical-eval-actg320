# Version 3 grading

Version 3 targets the one weak spot version 2 exposed: reasoning about what a data file's structure can and cannot record. I tested three candidate questions as probes first (see `v3/probes/`). Only the question on AIDS-defining event rates failed both models, so it became version 3 unchanged. I then wrote this rubric and ran both models fresh on October 21, 2026. Each had Python, the prompt and the data folder, and nothing else.

## Scores

| Model | Positive points | Penalties | Score |
|---|---|---|---|
| Claude Sonnet | 8 / 19 | −5 | 16% |
| Claude Opus | 8 / 19 | −3 | 26% |

## Criterion by criterion

| # | Sonnet | Opus | Evidence (Sonnet / Opus) |
|---|---|---|---|
| 1 | Pass | Pass | Row C, 52 and 27 / "AIDS diagnosis as the first event ... 52, 27" |
| 2 | Pass | Pass | 353.2 and 372.2 person-years / same |
| 3 | Pass | Pass | 14.72, 7.25, rate ratio 0.49 / same |
| 4 | **Fail** | **Fail** | Neither says the file cannot record a second AIDS diagnosis. Both describe `censor` as a first event but treat that as an ambiguity about deaths only. |
| 5 | **Fail** | **Fail** | Neither raises that 91 can include repeat events. Opus suggests the figure is "misquoted or comes from a different count." |
| 6 | **Fail** | **Fail** | "Person-time is the same under every definition" / "Person-time is the same as above, because follow-up stops at the first event" |
| 7 | Pass | Pass | Recommends reporting the composite as "first AIDS-defining event or death" / "describe them as AIDS-defining events or death" |
| 8 | Pass | Pass | Both note the 17 same-day deaths may hide an AIDS diagnosis |
| N1 | **Triggered** | **Triggered** | "The paper's 91 (60 and 31) falls inside that range. It would be reproduced if 3 control and 2 indinavir deaths had no prior AIDS diagnosis" / "a true AIDS-only count falls between 52 and 63 for control and between 27 and 33 ... both are inside those ranges" |
| N2 | **Triggered** | Not triggered | Row B: paper's 60 and 31 over the file's first-event person-time, 16.99 and 8.33 / Opus did not compute this |
| N3 | Not triggered | Not triggered | Both say the file matches the paper's composite and death counts |
| N4 | Not triggered | Not triggered | Both label the 63 and 33 as AIDS or death. Sonnet adds that calling it AIDS-defining events "is only approximate," a hedge that stops short of this error. |

Both models made the same core mistake. They read the paper's 91 as a number of patients and fitted it into the 79 to 96 range the file allows, so they never considered repeat diagnoses. Treating every count as one-per-patient also led both to use person-time that stops at the first event. For a rate of all events, person-time has to continue to death or censoring.

## Reproducibility

The probe runs of this same prompt (`v3/probes/p3_*.md`) made the same errors. Scored with this rubric, both probe runs come to 16%: each fails criteria 4, 5 and 6, and each triggers N1 and N2. Opus's probe run went further and named a specific split that would reconcile the counts ("8 of the 11 control cases and 4 of the 6 indinavir cases"). Two independent runs per model failed the same way. I wrote the rubric after reading the probe runs, so their scores are supporting evidence; the fresh runs are the primary result.

## Independent check

A separate grader, given the rubric, prompt, reference answer and both responses but not this file, reached the same verdict on every criterion and the same scores (16% and 26%). It flagged some rubric wording as open to interpretation, and I have left the rubric unchanged after grading:

- **Criterion 4.** It doesn't say whether a response must state the consequence (repeat diagnoses can't be counted) or only that follow-up stops at the first event. Both graders required the consequence.
- **Criterion 7.** "The rate it reports" is unclear when a response gives several rates.
- **N2 and N4.** It's unclear whether a caveat ("conditional on the paper," "only approximate") offsets the error. Both graders triggered N2 and did not trigger N4 for Sonnet.
- **Weighting.** Criteria 4, 5, 6 and N1 put most of the points on one insight. Responses that miss it bunch near zero, so the rubric separates seeing the insight from missing it more than it ranks partial answers.

## Unscored errors and checks

| Claim | Response | Data |
|---|---|---|
| Three patients have a `txgrp` code that doesn't match `tx` | Opus | **Wrong.** Groups 3 and 4 are the stavudine versions of each arm (codebook), so `tx` matches for all three |
| The 91/60/31 figure is "misquoted" | Opus | **Wrong.** The figures are verbatim from the paper |
| 128,991 and 135,950 days of follow-up | Sonnet | Correct |
| 45 and 25 non-fatal AIDS events; rates 12.74 and 6.72; rate ratio 0.53 | Sonnet | Correct |
| Rate difference 8.97 per 100 person-years (3.6 to 14.3); exact conditional CI 0.32 to 0.77 | Both | Correct |
