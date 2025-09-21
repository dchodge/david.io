---
title: SeroJump Widget
summary: Interactive widget for serojump - Individual Antibody Trajectories with Bayesian Inference
tags:
- widgets
date: "2025-01-15T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: https://seroanalytics.org/serojump-widget/

image:
  caption: SeroJump Widget - Interactive Bayesian Analysis
  focal_point: Smart
---

Interactive widget for _serojump_ - Individual Antibody Trajectories with Bayesian Inference

A tool to help users understand how _serojump_ infers missed infections using simulated data. Upload your own serological data or generate simulated trajectories to explore infection timing and antibody kinetics through Bayesian analysis.

## Features

- Upload CSV serological data or generate simulated trajectories
- Interactive MCMC parameter adjustment
- Real-time Bayesian inference visualization
- Individual infection probability analysis
- Convergence diagnostics and parameter trace plots
- Posterior analysis and timing accuracy assessment

**Note:** _serojump_ is computationally intensive, so this in-browser app may perform poorly on machines with low computational power. We recommend starting with short runs (≤2000 steps) for better performance.

## Reference

Hodgson D, Hay J, Jarju S, Jobe D, Wenlock R, et al. (2025) _serojump_: A Bayesian tool for inferring infection timing and antibody kinetics from longitudinal serological data. PLOS Computational Biology 21(9): e1013467
