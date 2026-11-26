+++
# Research themes strip: four boxes linking to project pages.
# Paper counts are calculated from each publication's `projects:` list.
widget = "themes"
headless = true
active = true
weight = 22        # after About (20)

heading = "Research themes"

[[items]]
  name = "RSV & vaccine policy"
  icon = "fas fa-syringe"
  blurb = "Transmission models and cost-effectiveness of RSV and influenza immunisation programmes."
  projects = ["cea_rsv", "cea_flu"]
  link = "/project/cea_rsv/"
[[items]]
  name = "Serological inference"
  icon = "fas fa-vial"
  blurb = "Inferring infection histories and correlates of protection from serological data."
  projects = ["imm_sero", "imm_seroanal"]
  link = "/project/imm_sero/"
[[items]]
  name = "Immune kinetics"
  icon = "fas fa-chart-line"
  blurb = "Mechanistic models of antibody and B cell dynamics after infection and vaccination."
  projects = ["imm_inhost"]
  link = "/project/imm_inhost/"
[[items]]
  name = "Bayesian methods & tools"
  icon = "fas fa-dice"
  blurb = "MCMC samplers, R packages and interactive widgets for inference."
  projects = ["bayes_transdim", "bayes_discrete"]
  link = "/software/"
  link_label = "Tools"
+++
