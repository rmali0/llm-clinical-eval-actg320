I'm adding a second part to the ACTG 320 teaching case. The data file (actg320.csv) and its codebook are in the data folder. For reference, here is what the trial report (Hammer et al., N Engl J Med 1997) says about eligibility and results:

- Patients had to be more than 16 years old, have a CD4 count of 200 per cubic millimeter or less within the 60 days before entry, have at least 3 months of prior zidovudine, and have a Karnofsky score of 70 or more. They were randomized between January 29, 1996, and January 27, 1997.
- 1,156 patients were randomized. AIDS or death occurred in 33 of 577 patients on indinavir and 63 of 579 on the control regimen (hazard ratio 0.50, 95% CI 0.33 to 0.76, P = 0.001). There were 8 and 18 deaths (hazard ratio 0.43, 95% CI 0.19 to 0.99, P = 0.04), and 91 AIDS-defining events in all.

Please work through the following and show the numbers behind each answer.

1. Check the file against the eligibility criteria and flag any values that look impossible. Which patients should I drop before rerunning the efficacy analysis?
2. Our file has 1,151 patients, and my stratified Cox model for death gives P = 0.048, not 0.04. I suspect the file lost some events along the way. Reconcile the file with the published counts and P-values.
3. For one slide I need a single number: how much does an AIDS-defining diagnosis raise the hazard of death? Give the hazard ratio and 95% CI, and say how you modeled it.
4. I'd also like to show that indinavir improved survival after an AIDS diagnosis, by comparing deaths after diagnosis between the arms among patients who developed AIDS. Can the data support that?

Finish with a short table of the key numbers.
