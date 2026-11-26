---
title: Software & Tools
type: software
summary: R packages, interactive widgets and dashboards for serological modelling, Bayesian inference and phylodynamics.
intro: |
  Open-source tools I build and maintain. Most come with an interactive widget so you can try the method in your browser before installing anything.

# Each group renders as a section; each tool as a card.
# Link keys (all optional): try, github, docs, paper
groups:
  - name: R packages
    tools:
      - name: serojump
        pitch: Infer infection timing and antibody kinetics from longitudinal serology using reversible-jump MCMC.
        lang: R
        try: https://seroanalytics.org/serojump-widget/
        github: https://github.com/seroanalytics/serojump
        paper: /publication/25_serojump/
      - name: seroCOP
        pitch: Bayesian inference for correlates of protection from serological data.
        lang: R
        try: https://seroanalytics.org/seroCOP-web/
        github: https://github.com/seroanalytics
      - name: rjmc
        pitch: Trans-dimensional (reversible-jump) MCMC samplers for parameter spaces that change in size.
        lang: R
        docs: https://dchodge.github.io/rjmc/
        github: https://github.com/dchodge/rjmc
      - name: ptmc
        pitch: MCMC samplers for exploring discrete and multimodal parameter spaces.
        lang: R
        docs: https://dchodge.github.io/ptmc/
        github: https://github.com/dchodge/ptmc

  - name: Platforms
    tools:
      - name: seroanalytics.org
        pitch: A hub of methods, tutorials and tools for serological modelling.
        lang: Web
        try: https://seroanalytics.org/
        github: https://github.com/seroanalytics

  - name: Interactive widgets
    tools:
      - name: mcmcPainter
        pitch: Paint pictures using Bayesian inference. A playful way to see how MCMC explores a posterior.
        lang: Web
        try: https://mcmcpainter.davidhodgson.me/
      - name: RJMCMC mixture model
        pitch: Watch reversible-jump MCMC infer a mixture distribution when the number of components is unknown.
        lang: Web
        try: https://rjmcmixture.davidhodgson.me
      - name: Bayesian epidemic modelling
        pitch: Interactive tools for fitting and exploring Bayesian epidemic models.
        lang: Web
        try: http://bayesvac.davidhodgson.me/

  - name: Phylodynamics dashboards
    tools:
      - name: Bayesian phylodynamics
        pitch: Links molecular evolution to epidemiological dynamics with Bayesian inference.
        lang: Web
        try: https://dchodge.github.io/bayesianPhyloDashboard/
      - name: Felsenstein pruning
        pitch: Step through the pruning algorithm for computing likelihoods on phylogenetic trees.
        lang: Web
        try: https://dchodge.github.io/felsenPruneDashboard/
      - name: Molecular evolution
        pitch: Explore how sequences change over time under different substitution models.
        lang: Web
        try: https://dchodge.github.io/molecularEvoDashboard/

  - name: Code for papers
    compact: true
    tools:
      - name: rsv_sero_fudan
        pitch: RSV antibody kinetics and infection risk in Taizhou (BMC Med 2026)
        github: https://github.com/dchodge/rsv_sero_fudan
        paper: /publication/26_rsv_china/
      - name: ab_boosting_published
        pitch: Pre-vaccination titre and influenza vaccine immunogenicity (Vaccine 2025)
        github: https://github.com/cmmid/ab_boosting_published
        paper: /publication/24_abkin/
      - name: covidbcell
        pitch: Memory B cell dynamics after ChAdOx1 and BNT162b2 (Front Immunol 2025)
        github: https://github.com/cmmid/covidbcell
        paper: /publication/24_bcell/
      - name: rsvmabmat
        pitch: Monoclonal antibodies vs maternal vaccination for RSV (Lancet Reg Health Eur 2024)
        github: https://github.com/cmmid/rsvmabmat
        paper: /publication/24_rsv_both/
      - name: nambcea
        pitch: Optimal nirsevimab programmes in England and Wales (Vaccine 2022)
        github: https://github.com/dchodge/nambcea
        paper: /publication/22_rsv_nam/
      - name: hero-study
        pitch: SARS-CoV-2 seroprevalence in UK healthcare workers (Wellcome Open Res 2022)
        github: https://github.com/cmmid/hero-study
        paper: /publication/22_covid_ab/
      - name: rsv_model_R_custom
        pitch: Next-generation RSV intervention strategies (BMC Med 2020)
        github: https://github.com/dchodge/rsv_model_R_custom
        paper: /publication/20_rsv_all/
---
