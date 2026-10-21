"""Reference solution for version 2 of the ACTG 320 evaluation task.

Reads data/actg320.csv and writes every value the version 2 rubric
checks to v2/solution/reference_values.json.

Run from the repository root:
    python v2/solution/reference_analysis.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from statsmodels.duration.hazard_regression import PHReg
from statsmodels.duration.survfunc import survdiff

ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data" / "actg320.csv")

# Published figures (Hammer et al., N Engl J Med 1997;337:725-33)
PAPER = {
    "randomized": 1156,
    "n_idv": 577,
    "n_control": 579,
    "primary_events_idv": 33,
    "primary_events_control": 63,
    "deaths_idv": 8,
    "deaths_control": 18,
    "aids_defining_events_all": 91,  # "including multiple events per patient"
}

# First-event type. A death is the first event when time_d equals time.
death_first = (df.censor_d == 1) & (df.time_d == df.time)
aids_first = (df.censor == 1) & ~death_first

ref = {"paper": PAPER}

# ---------------------------------------------------------------- Question 1
ref["q1"] = {
    "age_under_16": df.index[df.age < 16].tolist(),
    "age_values_under_16": df.age[df.age < 16].tolist(),
    "age_exactly_16_count": int((df.age == 16).sum()),  # ambiguous under "more than 16"
    "baseline_cd4_above_200_count": int((df.cd4 > 200).sum()),  # not a violation
    "baseline_cd4_above_200_strat2": df[df.cd4 > 200].strat2.value_counts().to_dict(),
    "baseline_cd4_zero_count": int((df.cd4 == 0).sum()),
    "priorzdv_min": float(df.priorzdv.min()),
    "karnofsky_min": int(df.karnof.min()),
    "priorzdv_top": sorted(df.priorzdv.tolist(), reverse=True)[:8],
    # 288 and 312 months mean zidovudine started in 1972-1973, about a decade
    # before HIV was identified (1983) and before zidovudine was used for it (1985).
    "priorzdv_288_or_more": df.index[df.priorzdv >= 288].tolist(),
    "priorzdv_above_138": int((df.priorzdv > 138).sum()),  # 138 months = July 1985 to January 1997
}

# ---------------------------------------------------------------- Question 2
n = df.tx.value_counts()
ev = df.groupby("tx").censor.sum()
dth = df.groupby("tx").censor_d.sum()
st_lr, p_lr = survdiff(df.time_d, df.censor_d, df.tx, strata=df.strat2)
st_lr_u, p_lr_u = survdiff(df.time_d, df.censor_d, df.tx)
wald = PHReg(df.time_d, df[["tx"]], status=df.censor_d, strata=df.strat2, ties="efron").fit()
_, p_lr_primary = survdiff(df.time, df.censor, df.tx, strata=df.strat2)
ref["q2"] = {
    "file_n_idv": int(n[1]),
    "file_n_control": int(n[0]),
    "missing_idv": PAPER["n_idv"] - int(n[1]),
    "missing_control": PAPER["n_control"] - int(n[0]),
    "file_primary_events_idv": int(ev[1]),
    "file_primary_events_control": int(ev[0]),
    "file_deaths_idv": int(dth[1]),
    "file_deaths_control": int(dth[0]),
    "death_wald_p_stratified": float(wald.pvalues[0]),
    "death_logrank_p_stratified": float(p_lr),
    "death_logrank_p_unstratified": float(p_lr_u),
    "primary_logrank_p_stratified": float(p_lr_primary),
    "aids_first_events": int(aids_first.sum()),
    "rows_per_patient": 1,
}


# ---------------------------------------------------------------- Question 3
def counting_process_cox(start, stop, event, X, strata):
    """Cox partial likelihood with delayed entry and Efron ties. Returns coefs and SEs."""

    def negll(beta):
        total = 0.0
        for s in np.unique(strata):
            m = strata == s
            xs, st, sp, e = X[m], start[m], stop[m], event[m]
            eta = xs @ beta
            r = np.exp(eta)
            for t in np.unique(sp[e == 1]):
                at_risk = (st < t) & (sp >= t)
                dead = (sp == t) & (e == 1)
                d = dead.sum()
                big_r, d_r = r[at_risk].sum(), r[dead].sum()
                total += eta[dead].sum() - sum(np.log(big_r - k / d * d_r) for k in range(d))
        return -total

    k = X.shape[1]
    beta = minimize(negll, np.zeros(k), method="BFGS").x
    h, eps = np.zeros((k, k)), 1e-4
    for i in range(k):
        for j in range(k):
            ei, ej = np.eye(k)[i] * eps, np.eye(k)[j] * eps
            h[i, j] = (
                negll(beta + ei + ej) - negll(beta + ei - ej) - negll(beta - ei + ej) + negll(beta - ei - ej)
            ) / (4 * eps * eps)
    return beta, np.sqrt(np.diag(np.linalg.inv(h)))


def hr(b, se):
    return {"hr": float(np.exp(b)), "ci_low": float(np.exp(b - 1.96 * se)), "ci_high": float(np.exp(b + 1.96 * se))}


def time_varying_aids_hr(covariates=(), stratify=False):
    """HR for AIDS as a time-dependent covariate, adjusted for `covariates`.

    Start-stop data: each patient whose first event was AIDS contributes
    (0, time] with AIDS = 0 and (time, time_d] with AIDS = 1. Use this to
    recompute the reference value for any adjustment set a response reports.
    """
    cols = ["aids", *covariates]
    rows = []
    for i, r in df.iterrows():
        base = [r[c] for c in covariates]
        if aids_first[i]:
            rows.append([0, r.time, 0, 0, *base, r.strat2])
            rows.append([r.time, r.time_d, r.censor_d, 1, *base, r.strat2])
        else:
            rows.append([0, r.time_d, r.censor_d, 0, *base, r.strat2])
    ss = pd.DataFrame(rows, columns=["start", "stop", "event", *cols, "strat2"])
    strata = ss.strat2.values if stratify else np.zeros(len(ss))
    b, se = counting_process_cox(
        ss.start.values, ss.stop.values, ss.event.values, ss[cols].values.astype(float), strata
    )
    return hr(b[0], se[0])


tv_unadj = time_varying_aids_hr()
tv_adj = time_varying_aids_hr(["tx"], stratify=True)
tv_adj_unstrat = time_varying_aids_hr(["tx"])
tv_full = time_varying_aids_hr(["tx", "cd4", "karnof", "age"], stratify=True)

# The trap: AIDS as a fixed "ever diagnosed" flag measured from randomization
fixed = df.assign(aids=aids_first.astype(int))
f1 = PHReg(fixed.time_d, fixed[["aids"]], status=fixed.censor_d, ties="efron").fit()
f2 = PHReg(fixed.time_d, fixed[["aids", "tx"]], status=fixed.censor_d, strata=fixed.strat2, ties="efron").fit()

# Cross-check: crude death rate after AIDS vs in AIDS-free follow-up
a = df[aids_first]
rate_after = a.censor_d.sum() / (a.time_d - a.time).sum()
rate_free = death_first.sum() / np.where(aids_first, df.time, df.time_d).sum()

ref["q3"] = {
    "time_varying_unadjusted": tv_unadj,
    "time_varying_adjusted_tx_stratified": tv_adj,
    "time_varying_adjusted_tx_unstratified": tv_adj_unstrat,
    "time_varying_adjusted_tx_cd4_karnof_age_stratified": tv_full,
    "fixed_ever_aids_unadjusted": {"hr": float(np.exp(f1.params[0])), "ci": np.exp(f1.conf_int()[0]).tolist()},
    "fixed_ever_aids_adjusted": {"hr": float(np.exp(f2.params[0])), "ci": np.exp(f2.conf_int()[0]).tolist()},
    "crude_rate_ratio": float(rate_after / rate_free),
    "deaths_after_aids": int(a.censor_d.sum()),
    "deaths_without_prior_aids": int(death_first.sum()),
}

# ---------------------------------------------------------------- Question 4
post = a.assign(t=a.time_d - a.time)
fp = PHReg(post.t, post[["tx"]], status=post.censor_d, ties="efron").fit()
ref["q4"] = {
    "aids_patients_by_arm": a.tx.value_counts().sort_index().to_dict(),
    "deaths_after_aids_by_arm": a.groupby("tx").censor_d.sum().to_dict(),
    "post_aids_cox_hr": float(np.exp(fp.params[0])),
    "post_aids_cox_ci": np.exp(fp.conf_int()[0]).tolist(),
    "post_aids_cox_p": float(fp.pvalues[0]),
}

out = ROOT / "v2" / "solution" / "reference_values.json"
out.write_text(json.dumps(ref, indent=2, default=str))
print(json.dumps(ref, indent=2, default=str))
