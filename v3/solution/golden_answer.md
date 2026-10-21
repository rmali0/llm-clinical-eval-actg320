# Version 3 reference answer

Values come from `v3/solution/reference_analysis.py`. The paper (Hammer et al., N Engl J Med 1997) states: "In all, there were 91 AIDS-defining events (including multiple events per patient). Sixty of these occurred among the patients assigned to receive zidovudine (or stavudine) and lamivudine, as compared with 31 among the patients assigned to indinavir, zidovudine (or stavudine), and lamivudine."

## What the file can count

The file has one row per patient. It records the first endpoint event (an AIDS-defining diagnosis or death, `time` and `censor`) and death (`time_d` and `censor_d`). It does not record any AIDS-defining diagnosis after the first one.

| | Control | Indinavir |
|---|---|---|
| First AIDS diagnosis before death or censoring | 52 | 27 |
| Person-years to first event or censoring | 353.2 | 372.2 |
| Rate of first AIDS diagnosis per 100 person-years | 14.7 (11.0 to 19.3) | 7.3 (4.8 to 10.6) |
| Rate ratio, indinavir vs control | | 0.49 (0.31 to 0.78) |

These are rates of a first diagnosis, not of all AIDS-defining events. The 17 deaths recorded as the first event (11 control, 6 indinavir) could include AIDS diagnoses made on the day of death, so 52 and 27 are minimum counts.

## Why the file can't line up with 91

The paper's 91 counts events, and some patients had more than one. It is not a count of patients, so it can't be compared with the 79 patients whose first event was AIDS, and the gap is not a sign of missing records. Because the 91 includes repeats, fewer than 91 patients had an AIDS diagnosis: somewhere between 79 and 90.

## A rate of all AIDS-defining events

Patients remain at risk of further AIDS-defining diagnoses after the first one, so a rate of all events needs person-time that runs to death or censoring (`time_d`): 377.7 control and 385.8 indinavir person-years. With the paper's counts:

| | Control | Indinavir |
|---|---|---|
| All AIDS-defining events (paper) | 60 | 31 |
| Person-years to death or censoring | 377.7 | 385.8 |
| Rate per 100 person-years | 15.9 (12.1 to 20.4) | 8.0 (5.5 to 11.4) |
| Rate ratio, indinavir vs control | | 0.51 (0.33 to 0.78) |

Stopping person-time at the first event (353.2 and 372.2 person-years) leaves out the time in which repeat events happened, which overstates both rates (17.0 and 8.3). The rate ratio moves little either way.
