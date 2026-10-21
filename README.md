# Clinical LLM evaluation sample: ACTG 320

Evaluation tasks I designed to test whether an AI model can analyze and interpret a randomized HIV treatment trial correctly. There are three versions, each built on what the previous one showed. Each has a task prompt, a reference solution computed in code, a weighted scoring rubric, and model responses graded against that rubric. Version 1 tested standard trial analysis, version 2 added classic analytic traps, and version 3 targets the one weak spot version 2 exposed.

## The trial and the data

ACTG 320 compared zidovudine (or stavudine) plus lamivudine, with or without indinavir, in 1,156 people with HIV and CD4 counts of 200 or fewer ([Hammer et al., N Engl J Med 1997](https://doi.org/10.1056/NEJM199709113371101)). The data file is the public teaching version of the trial from Hosmer, Lemeshow and May, *Applied Survival Analysis* (2nd ed., Wiley, 2008), which has 1,151 patients. I converted it from the copy distributed with scikit-survival (`actg320.arff`) to CSV without changing any values.

The file reproduces the published results: hazard ratio 0.50 (95% CI 0.33 to 0.76) for AIDS or death, and 0.43 (0.19 to 0.99) for death.

The regimens tested in ACTG 320 are no longer how HIV treatment starts today. I chose the trial because its data are public, its published results give a fixed benchmark to check against, and its structure supports the analytic traps these tasks test.

## Version 1: standard trial analysis

The prompt reads like a request from a colleague preparing a teaching session. Each question has a specific point where an analysis can go wrong:

| Question | What it checks |
|---|---|
| 1. Primary effect | Recognizing the endpoint is AIDS **or death**, and stratifying by the screening CD4 stratum (`strat2`) rather than regrouping the baseline `cd4` column. The two disagree for 88 patients. |
| 2. 48-week probability | Converting 48 weeks to day 336, reading a Kaplan-Meier estimate, and deriving the absolute difference and NNT. |
| 3. Death alone | Judging how much a 26-event result with an upper confidence bound near 1 can support. |
| 4. Subgroup claim | Rejecting "no effect" in a subgroup whose interval crosses 1 when the stratum HRs match and the interaction test shows no difference. |
| 5. First events | Separating deaths with no earlier AIDS diagnosis (17) from deaths after one (9), instead of counting all 26 deaths as endpoint deaths. |

The rubric has 21 binary criteria worth 47 points, plus 5 negative criteria for specific errors ([v1/rubric.md](v1/rubric.md)).

## Version 2: traps a careful analyst should catch

Version 1 didn't separate the models, so I rebuilt the task around errors that show up in real trial analyses. This time the prompt gives the published eligibility criteria and results, and each question carries a trap:

| Question | The trap |
|---|---|
| 1. Eligibility check | 82 patients have a baseline CD4 above 200, but eligibility used the screening count, so they are not violations. One patient aged 15 and three with 24 to 26 years of prior zidovudine are real problems. The colleague asks which patients to drop; the answer is none, because the trial was analyzed by intention to treat. |
| 2. Reconciling with the paper | The colleague suspects the file lost events. It didn't: every event count matches the paper. The P-value gap comes from Wald vs log-rank tests, and the paper's 91 AIDS-defining events include repeat diagnoses that a one-row-per-patient file cannot hold. |
| 3. AIDS and death | AIDS has to be a time-varying covariate. A fixed "ever had AIDS" flag gives 6.3 instead of 10.7 because of immortal time bias. |
| 4. Survival after AIDS by arm | Comparing arms among patients who developed AIDS conditions on an outcome of treatment, so randomization no longer protects the comparison. |

I wrote the rubric before running either model: 17 criteria worth 41 points, plus 5 negative criteria ([v2/rubric.md](v2/rubric.md)).

## Version 3: what the file can and can't record

In version 2, both models caught every classic trap. Sonnet's only miss was reading the paper's 91 AIDS-defining events as a sign of missing data. It didn't recognize that a file holding one first event per patient can't count repeat diagnoses. Version 3 targets that kind of reasoning.

I tested three candidate questions as probes first, each run blind on both models against pass criteria fixed in advance ([v3/probes](v3/probes)). Two of them (treating censoring as dropout, and splitting deaths by cause) didn't trip either model, so I dropped them. The third stumped both. It asks for the rate of AIDS-defining events by arm and for a check against the paper's 91 (60 control, 31 indinavir).

The paper's 91 counts events "including multiple events per patient." The file can only count patients whose first event was AIDS (52 and 27), and a rate of all events needs person-time that continues after a first diagnosis. Both models instead read 91 as a number of patients and fitted it inside the 79 to 96 range the file allows. Neither considered repeat diagnoses, and both stopped person-time at the first event.

I wrote the rubric after the probes and before a fresh pair of runs: 8 criteria worth 19 points, plus 4 negative criteria ([v3/rubric.md](v3/rubric.md)).

## Results

| Model | Version 1 | Version 2 | Version 3 |
|---|---|---|---|
| Claude Sonnet | 47 / 47 (100%) | 38 / 41 (93%) | 3 / 19 (16%) |
| Claude Opus | 47 / 47 (100%) | 41 / 41 (100%) | 5 / 19 (26%) |

All runs were blind, in Python, without the reference solutions. On version 3, the probe runs of the same prompt failed the same criteria as the fresh runs, so the failure reproduced across two independent runs per model. Opus also made two unscored errors: it called the paper's figures "misquoted" and claimed three treatment codes were inconsistent when they match the codebook. Grading notes, including the extra claims I checked against the data, are in each version's `model_runs/grading.md`.

## Repository layout

```
data/actg320.csv                    Trial data, 1,151 patients (shared by all versions)
data/codebook.md                    Variable definitions
v*/prompt.md                        The request given to each model
v*/rubric.md                        Scoring criteria
v*/solution/reference_analysis.py   Computes every value the rubric checks
v*/solution/reference_values.json   Output of the script
v*/solution/golden_answer.md        Reference answer
v*/model_runs/                      Model responses and grading
v3/probes/                          Candidate questions tested before version 3
```

## Reproduce the reference values

```
pip install -r requirements.txt
python v1/solution/reference_analysis.py
python v2/solution/reference_analysis.py
python v3/solution/reference_analysis.py
```

The version 2 script fits the time-varying Cox model directly from the partial likelihood, because the statsmodels Cox fit with delayed entry failed on this data. A crude rate ratio check (10.1) agrees with its estimate (10.7).

## Notes

The data comes from a published teaching dataset and is included unchanged so the analysis can be reproduced. Check the original source's terms before reusing it elsewhere.

I used Claude to run the blind model tests and to double-check the reference calculations.
