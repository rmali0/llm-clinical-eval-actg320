"""Reference solution for version 3 of the ACTG 320 evaluation task.

Reads data/actg320.csv and writes every value the version 3 rubric checks
to v3/solution/reference_values.json.

Run from the repository root:
    python v3/solution/reference_analysis.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data" / "actg320.csv")

# Paper: "In all, there were 91 AIDS-defining events (including multiple events
# per patient). Sixty of these occurred among the patients assigned to receive
# zidovudine (or stavudine) and lamivudine, as compared with 31 among the
# patients assigned to indinavir, zidovudine (or stavudine), and lamivudine."
PAPER_EVENTS = {"control": 60, "idv": 31, "total": 91}

ARMS = {"control": 0, "idv": 1}
DAYS_PER_YEAR = 365.25

death_first = (df.censor_d == 1) & (df.time_d == df.time)
aids_first = (df.censor == 1) & ~death_first


def poisson_ci(k, pt):
    """Exact 95% CI for a Poisson rate, per 100 person-years."""
    lo = chi2.ppf(0.025, 2 * k) / 2 if k > 0 else 0.0
    hi = chi2.ppf(0.975, 2 * k + 2) / 2
    return [100 * lo / pt, 100 * hi / pt]


def rate_ratio(k1, pt1, k0, pt0):
    """Rate ratio (arm 1 vs arm 0) with a log-scale Wald 95% CI."""
    rr = (k1 / pt1) / (k0 / pt0)
    se = np.sqrt(1 / k1 + 1 / k0)
    return {"rr": rr, "ci": [rr * np.exp(-1.96 * se), rr * np.exp(1.96 * se)]}


ref = {"paper_events": PAPER_EVENTS}

# Person-time that stops at the first event (AIDS, death or censoring): `time`.
# Person-time that runs to death or censoring: `time_d`. Patients stay at risk of
# further AIDS-defining events after a first diagnosis, so `time_d` is the
# denominator for a rate of all AIDS-defining events.
pt_first = {a: float(df[df.tx == t].time.sum() / DAYS_PER_YEAR) for a, t in ARMS.items()}
pt_total = {a: float(df[df.tx == t].time_d.sum() / DAYS_PER_YEAR) for a, t in ARMS.items()}
ref["person_years_to_first_event"] = pt_first
ref["person_years_to_death_or_censoring"] = pt_total

# What the file can count: first AIDS diagnosis before death or censoring.
first_aids = {a: int(aids_first[df.tx == t].sum()) for a, t in ARMS.items()}
ref["first_aids_diagnoses"] = first_aids
ref["first_aids_rate_per_100py"] = {
    a: {"rate": 100 * first_aids[a] / pt_first[a], "ci": poisson_ci(first_aids[a], pt_first[a])}
    for a in ARMS
}
ref["first_aids_rate_ratio"] = rate_ratio(first_aids["idv"], pt_first["idv"], first_aids["control"], pt_first["control"])

# Same-day ambiguity: deaths that were the first recorded event could include an
# AIDS diagnosis made on the day of death.
ref["deaths_as_first_event"] = {a: int(death_first[df.tx == t].sum()) for a, t in ARMS.items()}
ref["composite_events"] = {a: int(df[df.tx == t].censor.sum()) for a, t in ARMS.items()}

# Paper's all-event counts over person-time that runs to death or censoring
ref["paper_events_rate_per_100py_time_d"] = {
    a: {"rate": 100 * PAPER_EVENTS[a] / pt_total[a], "ci": poisson_ci(PAPER_EVENTS[a], pt_total[a])}
    for a in ARMS
}
ref["paper_events_rate_ratio_time_d"] = rate_ratio(
    PAPER_EVENTS["idv"], pt_total["idv"], PAPER_EVENTS["control"], pt_total["control"]
)

# The error: paper's all-event counts over person-time that stops at the first event
ref["paper_events_rate_per_100py_time_wrong"] = {
    a: 100 * PAPER_EVENTS[a] / pt_first[a] for a in ARMS
}

# Logical bound: the paper's 91 events include repeats, so fewer than 91 patients
# had an AIDS diagnosis; the file shows at least 79.
ref["patients_with_aids_bounds"] = {"min_from_file": int(aids_first.sum()), "max_given_repeats": 90}

out = ROOT / "v3" / "solution" / "reference_values.json"
out.write_text(json.dumps(ref, indent=2, default=float))
print(json.dumps(ref, indent=2, default=float))
