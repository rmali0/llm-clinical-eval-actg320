# Version 3 scoring rubric

Each criterion is scored pass or fail from the response text alone. Reference values are in `v3/solution/reference_values.json`. I wrote this rubric after the probe runs and before the fresh runs that are graded with it.

**Score** = (points from passed positive criteria minus points from triggered negative criteria) / 19, with a floor of 0.

## Positive criteria

| # | Criterion | Points |
|---|---|---|
| 1 | Reports first AIDS diagnoses by arm from the file: 52 control and 27 indinavir (79 in total, or "at least 79"). | 2 |
| 2 | Reports person-time to first event or censoring of about 353 (control) and 372 (indinavir) person-years. | 1 |
| 3 | Reports first-diagnosis rates of about 14.7 and 7.3 per 100 person-years and a rate ratio of about 0.49. | 2 |
| 4 | States that the file records only one endpoint event per patient (the first), so it cannot count repeat AIDS-defining diagnoses. | 4 |
| 5 | Raises that the paper's 91 may include more than one AIDS-defining event per patient, so it is a count of events rather than patients and cannot be matched to patient counts in the file. | 4 |
| 6 | States that a rate of all AIDS-defining events needs person-time that continues after a first diagnosis (to death or censoring, `time_d`), not person-time that stops at the first event. | 3 |
| 7 | Labels the rate it reports for what it is (first AIDS diagnosis, or AIDS or death), not as a rate of all AIDS-defining events. | 2 |
| 8 | Notes that the 17 deaths recorded as the first event may hide AIDS diagnoses made on the day of death. | 1 |

## Negative criteria

| # | Criterion | Points |
|---|---|---|
| N1 | Treats the paper's 91 (60 and 31) as a count of patients, for example by placing it within a range of 79 to 96 patients or explaining the gap as same-day AIDS diagnoses at death, without raising repeat events. | −3 |
| N2 | Pairs the paper's 60 and 31 events with person-time that stops at the first event (about 353 and 372 person-years, giving about 17.0 and 8.3 per 100 person-years). | −2 |
| N3 | Claims the file is missing AIDS events or deaths. | −3 |
| N4 | Presents the AIDS-or-death rate (63 and 33 events) as the rate of AIDS-defining events. | −3 |
