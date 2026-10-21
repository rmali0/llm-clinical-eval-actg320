# actg320.csv codebook

1,151 patients, one row per patient. Times are in days from enrollment.

| Column | Meaning | Values |
|---|---|---|
| time | Days to AIDS-defining diagnosis or death, or to censoring | 1 to 364 |
| censor | Event indicator for AIDS-defining diagnosis or death | 1 = event, 0 = censored |
| time_d | Days to death, or to censoring | 1 to 364 |
| censor_d | Event indicator for death only | 1 = died, 0 = censored |
| tx | Treatment indicator | 1 = regimen includes indinavir (IDV), 0 = control regimen without IDV |
| txgrp | Treatment group | 1 = ZDV + 3TC, 2 = ZDV + 3TC + IDV, 3 = d4T + 3TC, 4 = d4T + 3TC + IDV |
| strat2 | CD4 stratum at screening | 0 = CD4 of 50 or fewer, 1 = CD4 above 50 |
| sex | Sex | 1 = male, 2 = female |
| raceth | Race/ethnicity | 1 = White non-Hispanic, 2 = Black non-Hispanic, 3 = Hispanic, 4 = Asian or Pacific Islander, 5 = American Indian or Alaskan Native |
| ivdrug | History of IV drug use | 1 = never, 2 = current, 3 = previous |
| hemophil | Hemophilia | 1 = yes, 0 = no |
| karnof | Karnofsky performance score | 70, 80, 90, 100 |
| cd4 | Baseline CD4 count, derived from multiple measurements | cells per cubic millimeter |
| priorzdv | Months of prior zidovudine use | months |
| age | Age at enrollment | years |
