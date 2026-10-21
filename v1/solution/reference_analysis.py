"""Reference solution for version 1 of the ACTG 320 evaluation task.

Reads data/actg320.csv, computes every value the version 1 rubric checks,
and writes them to v1/solution/reference_values.json.

Run from the repository root:
    python v1/solution/reference_analysis.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.duration.hazard_regression import PHReg
from statsmodels.duration.survfunc import SurvfuncRight, survdiff

ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data" / "actg320.csv")

DAY_48_WEEKS = 48 * 7  # 336


def cox(time, event, covariates, strata=None):
    """Cox model with Efron ties. Returns HR, CI bounds and Wald p for the first covariate."""
    fit = PHReg(time, covariates, status=event, strata=strata, ties="efron").fit()
    ci = np.exp(fit.conf_int()[0])
    return {
        "hr": float(np.exp(fit.params[0])),
        "ci_low": float(ci[0]),
        "ci_high": float(ci[1]),
        "p": float(fit.pvalues[0]),
    }


def km_risk(time, event, day):
    """Kaplan-Meier cumulative probability of the event by `day`."""
    sf = SurvfuncRight(time, event)
    surv = sf.surv_prob[sf.surv_times <= day]
    return float(1 - surv[-1]) if len(surv) else 0.0


ref = {}

# Counts by arm
ref["n_by_arm"] = df.tx.value_counts().sort_index().to_dict()
ref["primary_events_by_arm"] = df.groupby("tx").censor.sum().to_dict()
ref["deaths_by_arm"] = df.groupby("tx").censor_d.sum().to_dict()

# Q1: primary endpoint, Cox stratified by the screening stratum (strat2)
ref["q1_primary_stratified_cox"] = cox(df.time, df.censor, df[["tx"]], df.strat2)
chi2, p = survdiff(df.time, df.censor, df.tx, strata=df.strat2)
ref["q1_stratified_logrank"] = {"chi2": float(chi2), "p": float(p)}
ref["q1_unstratified_cox"] = cox(df.time, df.censor, df[["tx"]])
# The trap: a stratum rebuilt from baseline cd4 does not match strat2
ref["q1_stratum_discordance"] = {
    "strat2_0_baseline_cd4_above_50": int(((df.strat2 == 0) & (df.cd4 > 50)).sum()),
    "strat2_1_baseline_cd4_50_or_less": int(((df.strat2 == 1) & (df.cd4 <= 50)).sum()),
}
ref["q1_wrong_stratum_cox"] = cox(df.time, df.censor, df[["tx"]], (df.cd4 <= 50).astype(int))

# Q2: Kaplan-Meier probability of the primary endpoint by 48 weeks (day 336)
risk_ctrl = km_risk(df.time[df.tx == 0], df.censor[df.tx == 0], DAY_48_WEEKS)
risk_idv = km_risk(df.time[df.tx == 1], df.censor[df.tx == 1], DAY_48_WEEKS)
ref["q2_km_48wk"] = {
    "control": risk_ctrl,
    "idv": risk_idv,
    "absolute_difference": risk_ctrl - risk_idv,
    "nnt": 1 / (risk_ctrl - risk_idv),
}

# Q3: death alone, same stratified model
ref["q3_death_stratified_cox"] = cox(df.time_d, df.censor_d, df[["tx"]], df.strat2)
ref["q3_death_unstratified_cox"] = cox(df.time_d, df.censor_d, df[["tx"]])

# Q4: stratum-specific effects and the treatment-by-stratum interaction
for s in (0, 1):
    d = df[df.strat2 == s]
    ref[f"q4_hr_strat2_{s}"] = cox(d.time, d.censor, d[["tx"]])
    ref[f"q4_events_strat2_{s}"] = int(d.censor.sum())
inter = df.assign(tx_x_strat2=df.tx * df.strat2)
ref["q4_interaction"] = cox(inter.time, inter.censor, inter[["tx_x_strat2", "tx"]], inter.strat2)

# Q5: first-event type. A death is the first event when time_d equals time.
death_first = (df.censor_d == 1) & (df.time_d == df.time)
aids_first = (df.censor == 1) & ~death_first
ref["q5_first_events"] = {
    "deaths_first": int(death_first.sum()),
    "aids_first": int(aids_first.sum()),
    "deaths_after_aids": int(((df.censor_d == 1) & (df.time_d > df.time)).sum()),
    "deaths_first_by_arm": df[death_first].tx.value_counts().sort_index().to_dict(),
    "aids_first_by_arm": df[aids_first].tx.value_counts().sort_index().to_dict(),
}

# Checks on extra claims made in the model responses (not scored)
at_risk = {int(t): int(((df.tx == t) & (df.time >= DAY_48_WEEKS)).sum()) for t in (0, 1)}
last_event = {int(t): int(df[(df.tx == t) & (df.censor == 1)].time.max()) for t in (0, 1)}
ref["extra_checks"] = {
    "at_risk_day_336_by_arm": at_risk,
    "last_primary_event_day_by_arm": last_event,
    "person_years": float(df.time.sum() / 365.25),
    "max_baseline_cd4_in_strat2_0": float(df[df.strat2 == 0].cd4.max()),
    "min_baseline_cd4_in_strat2_1": float(df[df.strat2 == 1].cd4.min()),
    "top_priorzdv_months": sorted(df.priorzdv.tolist(), reverse=True)[:3],
    "txgrp_by_tx": pd.crosstab(df.tx, df.txgrp).to_dict(),
}

out = ROOT / "v1" / "solution" / "reference_values.json"
out.write_text(json.dumps(ref, indent=2, default=str))
print(json.dumps(ref, indent=2, default=str))
