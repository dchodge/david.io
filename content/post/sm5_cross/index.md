---
title: "WHAT CAN I INFER FROM CROSS-SECTIONAL SEROLOGICAL DATA?"
subtitle: "A Practical Primer"
summary: ""
authors:
- admin
tags:
- serological modelling
- immune dynamics
- antibody kinetics
- infection timing
- Bayesian inference
categories:
- Serological Modelling
date: "2025-11-16T00:00:00Z"
lastmod: "2025-11-16T00:00:00Z"
featured: false
draft: false
---

Cross-sectional serological surveys, where blood samples are tested from a sample of people at a single point in time for antibodies, have become essential tools in modern epidemiology. These surveys provide a snapshot of population exposure to pathogens that case-based surveillance, such as PCR testing, often misses. This primer focuses on three key applications: estimating infection prevalence, assessing population-level immunity when correlates of protection exist, and using age-stratified data with serocatalytic models to understand transmission rates in the past.

## Inferring True Prevalence: Beyond Reported Cases

**What you can infer**: The most fundamental application of cross-sectional serology is estimating seroprevalence, the proportion of the population with detectable antibodies indicating past infection. This reveals the burden of infection, and it is particularly crucial for diseases with substantial asymptomatic or mild infections that evade clinical surveillance.

**Why it matters**: For many pathogens, reported cases represent only a fraction of actual infections. Serological surveys expose this "iceberg effect" by detecting antibodies in people who never sought testing or showed symptoms.


### Examples


1. [A 2020 study in Ischgl](https://www.nature.com/articles/s43856-021-00007-1), Austria, an early COVID-19 hotspot, found 42.4% seroprevalence when only 6.4% of residents having confirmed cases. This revealed that infections were nearly 7 times higher than reported, fundamentally changing the understanding of the outbreak's scope and the virus's transmissibility.

2. [Spain's ENE-COVID study](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)31483-5/fulltext) found 5% national seroprevalence in May 2020, implying over 2 million infections when only 250,000 cases had been reported, an ascertainment rate of approximately 12%. This demonstrated that ongoing virological surveillance was capturing only the most severe cases, missing the vast majority of infections. 

3. In endemic regions, [serological surveys consistently show 80-90% of adults are seropositive for hepatitis A](https://www.ncbi.nlm.nih.gov/books/NBK459290/), while clinical surveillance captures only a tiny fraction of cases. Most childhood infections are asymptomatic but confer lifelong immunity, a pattern only revealed through serology.

**Practical application**: Seroprevalence estimates are essential for calculating accurate infection fatality rates (IFR). By dividing deaths by seroprevalence-based infection estimates rather than reported cases, you obtain a realistic mortality risk. COVID-19 meta-analyses estimated global IFR at 0.15-0.5% based on seroprevalence studies, far lower than case fatality rates of 2-5% calculated from confirmed cases alone. This transformed risk communication and resource allocation decisions.

**Methodological considerations**: Seroprevalence estimates require adjustment for test sensitivity and specificity using the Rogan-Gladen estimator. You can do this in R using the epiR package.

True prevalence = (Apparent prevalence + Specificity - 1) / (Sensitivity + Specificity - 1)

In R we can calcualte the true prevalence using the `epiR` package:

```r
library(epiR) 
epi.prev(pos = 240, tested = 1000, se = 0.90, sp = 0.95)
```

## Population-Level Immunity and Susceptibility: When Correlates of Protection Exist

**What you can infer**: When a correlate of protection is established, that is, a threshold antibody level that predicts immunity against disease, cross-sectional serology becomes exceptionally powerful for assessing population vulnerability to future outbreaks.

**Correlates of protection**: These are antibody titers or seropositivity thresholds associated with protection from infection or disease. For measles, neutralizing antibody titers above ~120 mIU/mL generally indicate immunity. Also, for pertussis, specific IgG thresholds correlate with reduced disease risk (see [here](http://localhost:1313/post/sm4_cop2/) for a summary of correlate of protection thresholds for other pathogens!)

### Examples 

1. *Measles*: [The Samoa measles outbreak](https://pmc.ncbi.nlm.nih.gov/articles/PMC7533430/) in 2019 resulted in 5,707 cases and 83 deaths, with 87% of deaths occurring in children under 5 years. This outbreak was preceded by a decline in MMR vaccine uptake between 2013 and 2018, with first dose coverage dropping from 99% to 40% and second dose from 87% to 28%, falling well below the 95% coverage threshold needed to prevent outbreaks.
2. *Diphtheria*: [Serological surveys in the 1990s former Soviet Union](https://wwwnc.cdc.gov/eid/article/4/4/98-0404_article) revealed dramatically declining diphtheria antitoxin levels in adults as vaccination programs deteriorated. Population serosurveys showed <50% of adults had protective antibody levels, predicting the massive diphtheria epidemic that subsequently killed thousands. Early serological data could have justified urgent mass vaccination campaigns.
3. *Rubella*: Pre-vaccine era serological surveys showed [80-90% of women](https://pmc.ncbi.nlm.nih.gov/articles/PMC4992224/) of childbearing age had protective rubella antibodies from natural infection. Post-vaccination, serological surveillance monitors whether immunity gaps emerge in young adults, predicting congenital rubella syndrome risk. Countries introducing rubella vaccination use baseline serosurveys to identify susceptible cohorts requiring catch-up campaigns.

**Quantifying susceptible populations**: When you know both the correlate of protection and the herd immunity threshold, serology identifies precisely who remains vulnerable. If a pathogen requires 80% immunity and your survey shows 65% with protective antibodies, you know 15% additional immunity is needed and can target interventions accordingly.

**Geographic and demographic targeting**: Stratifying serological data by age, location, and demographics reveals where susceptible pockets exist. During measles outbreaks, serological surveys consistently identify under-vaccinated communities with <90% immunity—these become priority targets for rapid vaccination campaigns.

**Practical application**: Serological surveillance guides vaccine policy. If surveys show waning immunity in adolescents (e.g., pertussis antibodies declining 5-10 years after childhood vaccination), this justifies booster dose programs. Population serosurveys drove the addition of adolescent Tdap boosters in many countries when serological data revealed susceptibility gaps.


## Serocatalytic Models: Inferring Transmission Dynamics from Age-Prevalence Patterns

**What you can infer**: Serocatalytic models are mathematical frameworks that infer transmission dynamics from age-stratified seroprevalence data. These models are particularly powerful for endemic infections where you can assume relatively stable transmission over time.

**The catalytic principle**: In an endemic steady-state, age-seroprevalence curves reflect cumulative exposure. As individuals age, they progressively encounter the pathogen at rate λ (force of infection). The proportion seropositive at age a is: *P(a) = 1 - exp(-λa)*. By fitting this model to observed age-seroprevalence data, you estimate the force of infection, the rate at which susceptible individuals become infected per unit time.

### Examples

1. *General framework*: Serological surveys across age groups reveal characteristic patterns. If seroprevalence is 20% at age 5, 50% at age 10, 70% at age 15, and plateaus around 85% in adults, fitting a catalytic model estimates the force of infection at approximately 0.10-0.15 per year. This means susceptible individuals have 10-15% annual probability of infection. This force of infection estimate immediately informs vaccine policy. With λ = 0.12/year, the average age at infection is 1/λ ≈ 8 years. Vaccinating children at age 12-15 months misses the peak transmission period. School-entry vaccination (age 5-6) better matches the epidemiology.

2. *Hepatitis A*: [In high-endemicity settings](https://www.sciencedirect.com/science/article/pii/S2772368225001404), serological surveys indicate rapid increases in seroprevalence in early childhood, with approximately 60% seropositive by age 5 and 90% by age 18. Catalytic models estimate a very high force of infection (λ > 0.3/year) in young children, indicating intense faecal-oral transmission. As sanitation improves, repeated surveys show declining force of infection and older age at infection, the "hygiene paradox" where improved conditions paradoxically increase disease severity by delaying infection to adulthood.

**Reversible catalytic models**: Basic models assume lifelong seropositivity; however, some pathogens exhibit antibody waning (seroreversion). Reversible catalytic models incorporate both infection rate λ and seroreversion rate ρ:

dS/dt = ρR - λS

dR/dt = λS - ρR

Where S = seronegative proportion, R = seropositive proportion.

3.  *RSV*: Serological surveys show nearly universal childhood exposure (>90% seropositive by age 3) but [declining seroprevalence in adults](https://pmc.ncbi.nlm.nih.gov/articles/PMC11126071/), suggesting antibody waning. Reversible catalytic models estimate both high force of infection in children (λ ≈ 0.5-1.0/year) and moderate seroreversion rates in adults, explaining why elderly populations show only 60-70% seropositivity despite repeated lifetime exposures.

**Time-varying force of infection with repeated surveys**: Multiple cross-sectional surveys over years enable estimation of temporal changes in transmission intensity. Each survey provides an age-seroprevalence snapshot; together they reveal how the force of infection has changed.

4. *Endemic measles*: Historical serological surveys from pre-vaccine era show high, stable force of infection. Following the introduction of the vaccine, repeated surveys show a declining force of infection as vaccination reduces transmission. Age-seroprevalence curves flatten as fewer susceptible individuals encounter the virus. 


## Methodological implementation:
There are [several packages in R](https://seroanalytics.org/) to run serocatalytic models. One example of how to fit a costant FoI serocatalytic model is below

```r
library(serofoi) # Fit basic catalytic model 

data(chagas2012) # get data
plot_serosurvey(chagas2012, bin_serosurvey = TRUE, size_text = 15) # plot data
seromodel <- fit_seromodel(serosurvey = chagas2012) # fit foi model


# Mode complex FoI models can be implented with the Rsero and the serosv packages. 

```


### Practical applications: 
Force of infection estimates guide multiple policy decisions:

* *Optimal vaccination age*: Vaccinate just before peak force of infection to maximize protection during high-risk period
* *Required vaccination coverage*: Higher force of infection demands higher coverage to achieve herd immunity
* *Outbreak prediction*: Rising force of infection in susceptible cohorts predicts impending outbreaks
* *Disease elimination feasibility*: Very high endemic force of infection (λ > 0.5/year) requires sustained high-coverage vaccination; diseases with lower force of infection are easier elimination targets

### Key Methodological Limitations

Across all applications, several limitations apply:

**Selection bias**: Who participates profoundly affects results. Blood donor samples exclude very young, very old, and sick individuals. Household surveys may miss institutionalised or homeless populations. Always consider sample representativeness.

**Test performance**: Adjust for sensitivity and specificity. Low specificity can inflate prevalence estimates, particularly when the true prevalence is low. High specificity is most important at low prevalence, while high sensitivity is most important at high prevalence.

**Antibody waning**: Declining antibody levels over time mean that seroprevalence underestimates the cumulative number of infections. This is particularly problematic for mild infections or pathogens with short-lived responses. Measuring antibody titers and trying to understand the kinetics (not just seropositivity) can partially address this.

**Cross-reactivity**: Related pathogens may produce antibodies that cross-react with each other. Dengue serology is notoriously complicated by cross-reactivity among its four serotypes. Coronavirus antibody assays may detect antibodies from common cold coronaviruses, inflating apparent SARS-CoV-2 seroprevalence.

### Summary

Cross-sectional serological surveys provide a powerful lens into the true scope of infectious disease transmission, revealing the vast landscape of infections that lie beneath the surface of reported cases. By capturing both symptomatic and asymptomatic infections, these surveys change our understanding of disease burden, transmission dynamics, and population-level immunity.
The examples above, from COVID-19's iceberg effect in Ischgl to Spain's nationwide seroprevalence data and the hidden reservoir of hepatitis A, demonstrate that what we see through clinical surveillance is often just a fraction of reality. This insight has profound implications: it enables more accurate IFR calculations that inform public health responses, reveals the true extent of population immunity that guides vaccination strategies, and helps identify high-risk groups that might otherwise remain invisible.

Yet serological data is only as good as our ability to interpret it correctly. Understanding the nuances of antibody testing, accounting for waning immunity over time, and properly modelling age-stratified patterns are all essential for extracting reliable insights. As we continue to refine these methods and expand their application, cross-sectional serology will remain an indispensable tool for bridging the gap between what we observe and what is truly happening in our populations.

The next time you see a case count, remember: the true story is likely much larger, and serology helps us read between the lines.

