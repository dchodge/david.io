---
title: "CORRELATES OF PROTECTION: FUMBLING THROUGH THE TERMINOLOGY"
subtitle: "The (confusing) statistical frameworks that could accelerate vaccine approvals"
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
date: "2025-10-05T00:00:00Z"
lastmod: "2025-10-05T00:00:00Z"
featured: false
draft: false
---
Long ago, Edward Jenner made medical history by inoculating a young boy with cowpox and demonstrating protection against smallpox. Jenner had no idea *why* it worked, he just rolled with it, and thus inoculation was born. For nearly two centuries, vaccine developers operated in a similar vein, testing their creations in large populations and hoping for the best, often without fully understanding the biological mechanisms working underneath.

Today, scientists have a powerful tool that Jenner could only dream of: correlates of protection. These biological markers can predict whether a vaccine will work before testing it in tens of thousands of people, transforming how we develop vaccines, potentially saving years of research time and billions of dollars. But the terminology around these correlates is notoriously confusing and has caused me many hours of sighing and furrowing my brow. Therefore, I thought I'd provide a light introduction to the essential concepts.

## What Exactly Is a Correlate of Protection?

Simply, a correlate of protection is a measurable biomarker that tells us someone is protected against a disease. It's a biological readout, and is usually something we can measure in blood that correlates with protection from infection and/or disease.

The most common correlate of protection is antibody levels. For many diseases, having a certain level of antibodies means you're protected. It's like checking the oil level in your car, if it's above a certain mark, you're good to go.

But here's where it gets tricky. Not all correlates are created equal, and scientists use different terms to describe different types of relationships between immune markers and protection.

## Core Conceptual Distinctions

The field of correlates has a terminology problem that stems from decades of incremental research. Different scientists coined different terms, and now we're stuck with a somewhat muddled lexicon.

The most important distinction is between a **correlate of protection** and a **mechanistic correlate of protection** (also called a **surrogate endpoint**).

A correlate of protection is simply statistical: when this marker goes up, protection goes up too. But correlation doesn't equal causation. Maybe those antibodies aren't actually doing the protecting; they're just a sign that something else protective is happening.

A mechanistic correlate (or surrogate endpoint) is the gold standard: it's a marker that actually *causes* protection. These are the antibodies or immune cells that physically prevent infection or disease. If we could give someone those exact antibodies artificially, they'd be protected.

**Protection from infection vs. disease:** Researchers distinguish between **correlates of protection from infection** (you don't get infected at all) and **correlates of protection from disease** (you might get infected but don't get sick). This matters enormously for diseases like COVID-19, where vaccines that prevent severe illness but not infection have different correlates than those that prevent all infection.

Then there's the flip side: **correlates of risk**. While correlates of protection tell us who's safe, correlates of risk identify who's vulnerable. For example, in HIV vaccine trials, researchers discovered that certain antibody responses actually correlated with *increased* infection risk, a devastating finding that helped explain why some vaccine candidates failed. Understanding both sides of the coin is crucial: we need to know not just what protects, but what fails to protect or even increases susceptibility.

Why is the terminology so messy? Because the field evolved piecemeal. Early vaccine researchers simply noticed that antibody levels seemed to predict protection. As immunology advanced, scientists realised the relationship was more complex; sometimes T cells matter more than antibodies, sometimes antibodies correlate with protection but don't cause it. Each discovery spawned new terminology, but no one went back to standardise everything.

## From Concepts to Proof: Two Different Paths

The path to establishing a correlate of protection depends on where you're starting from:

### Path 1: Natural History Studies

Sometimes we identify correlates by studying people who've been naturally infected or exposed. Researchers measure immune markers in these individuals and observe who gets infected or sick. This reveals immune markers that associate with protection in natural settings.

For example, studies of naturally infected individuals might show that people with antibody levels above a certain threshold rarely get reinfected. This is incredibly valuable for understanding immunity and setting targets for vaccine development.

**The limitation:** Without randomisation, we can't definitively prove causation. Maybe people with high antibodies are different in other ways, prior exposures, genetics, behaviour. The antibodies might be protective, or they might just be a sign of a robust immune system that protects through other mechanisms too.

### Path 2: Vaccine Trial Validation

Once we have a vaccine candidate, we can use randomised controlled trials to rigorously test whether an immune marker truly predicts protection. The key advantage: randomisation eliminates confounding. If vaccinated people with high antibody levels are protected while unvaccinated people with naturally high antibody levels aren't (or vice versa), we learn something crucial about whether those antibodies are truly involved in the mechanism for protection.

**The challenge:** How do you *prove* that an immune marker is a valid surrogate for vaccine efficacy? If regulators could confidently say "antibodies above level X mean this vaccine works," then new vaccines could be approved based on antibody measurements alone, without massive clinical trials testing disease outcomes. This would save years and billions of dollars and potentially countless lives by accelerating vaccine development for emerging threats.

But to make such claims, we need rigorous statistical evidence from vaccine trials. We need to distinguish between:

- A marker that simply *associates* with protection (it goes up when protection goes up)
- A marker that *predicts* vaccine efficacy (if it's high in vaccinees, we can reliably expect protection)
- A marker that *causes* protection (the marker itself is the mechanism doing the protecting)

This is where statistical frameworks come in. They provide formal mathematical methods to test whether an immune marker deserves to be called a true "surrogate endpoint", that is, one that can replace clinical disease outcomes in future vaccine trials for regulatory approval. T

Two major approaches emerged to tackle this challenge, each with different philosophies about how strict the evidence needs to be. **Importantly, these frameworks are specifically designed for randomised vaccine trials**, not observational studies of natural immunity.

## Statistical Frameworks for Vaccine Trials: Attempting to Clean Up the Mess

### The Prentice Criterion (1989): The Strict Approach

The Prentice criterion established four statistical tests for validating a surrogate endpoint:

(1) treatment must affect the clinical outcome,

(2) treatment must affect the surrogate,

(3) the surrogate must associate with the clinical outcome, and

(4) the treatment effect on the clinical outcome must be captured by the surrogate.

Prentice is essentially trying to prove mechanistic causation, that is, an immune marker is actually *causing* the protection, not just correlating with it. The fourth criterion is the most critical and difficult: it requires demonstrating no relationship between treatment and survival after accounting for the surrogate outcome. In other words, once you control for the immune marker, vaccination status shouldn't matter anymore because all the vaccine's effect should flow through that marker.

**The problem?** Prentice's approach assumes the surrogate explains 100% of vaccine efficacy, which proved too restrictive. Even today there's only one commonly reported correlate for an infectious disease which meets Prentice criteria: HAI titers from a 1943 influenza outbreak. In reality, immunology is messier because maybe the antibodies are doing *some* of the protecting while perhaps T cells do the rest, or maybe the antibodies we're measuring are just a shadow of the real protective mechanism.

This all-or-nothing standard has proven nearly impossible to meet. Most immune markers we rely on in practice, including the widely-used pneumococcal vaccine antibody threshold, have never been proven to satisfy Prentice criteria, yet we still use them because they're the best predictors we have.

### The Qin/Gilbert Framework (2007-2008): Embracing the Complexity

Recognising the limitations of Prentice's all-or-nothing approach, researchers Li Qin, Peter Gilbert, and colleagues developed a more nuanced framework using causal inference methods. Instead of demanding proof that a marker causes 100% of protection, they proposed three distinct levels of immune correlates: "correlate of risk" (CoR), "level 1 surrogate of protection," and "level 2 surrogate of protection."

This hierarchy directly addresses both the terminology mess and the practical needs of vaccine development:

**Correlate of Risk (CoR):** An immune marker in a cohort of interest (such as vaccine recipients) that correlates with the clinical outcome. This is your basic statistical correlation and makes no claim about causation. The marker goes up, protection goes up (or down), but we're not saying *why*. This is the lowest bar but still useful as it tells us which markers are worth investigating further.

**Level 1 Surrogate of Protection:** An immune marker that can reliably predict vaccine efficacy in settings similar to the trial. We're moving beyond simple correlation toward something more robust, the marker not only correlates with protection but can actually predict the vaccine's efficacy in similar populations. But we're still not claiming the marker is the sole protective mechanism or that it would work the same way in very different contexts.

**Level 2 Surrogate of Protection:** A marker validated across multiple trials and populations. If it predicts protection across different contexts, e.g. different ages, different geographic regions, different viral strains, it's probably playing a causal role. This approaches the "gold standard" mechanistic correlate that Prentice was aiming for, but acknowledges that other immune factors may also contribute.

**How this framework differs**: Unlike Prentice's approach, the principal surrogate framework uses innovative trial designs and causal inference methods to handle missing data—like the fact that we can't measure vaccine-induced immune responses in placebo recipients. It doesn't demand that one marker explain everything, allowing for the messy reality where multiple immune components contribute to protection.

Critically, this framework can also identify situations where a marker correlates with *increased* risk rather than protection (exactly what happened in those failed HIV vaccine trials). The Qin/Gilbert approach can detect when certain immune responses predict harm rather than benefit, something simpler correlation approaches might miss.

### Comparing the Approaches

The fundamental difference: **Prentice tries to prove causation right out the gate; Qin/Gilbert creates a hierarchy from correlation to probable causation.**

- **Prentice:** *"These antibodies ARE doing the protecting (prove criterion 4: treatment effect fully captured)"*
- **Qin/Gilbert:** *"These antibodies might be just correlated (CoR), might be predictive in this context (Level 1), or might be broadly validated and probably causal (Level 2)"*

Both approaches face challenges with very high vaccine efficacy, where small numbers of breakthrough infections make the statistics difficult. But the Qin/Gilbert framework's flexibility and use of causal inference methods have made it increasingly preferred for modern vaccine trials.

Importantly, the Qin/Gilbert levels map onto the conceptual distinctions we discussed earlier:

- A **CoR** is just a statistical correlate; correlation without causation
- A **Level 1 surrogate** is a predictive marker in a specific context
- A **Level 2 surrogate** approaches being a true **mechanistic correlate,** validated widely enough that it probably reflects a causal protective mechanism

### Connecting Natural History to Vaccine Trials

These frameworks build on but are distinct from natural history correlates:

**Natural history studies** identify candidate correlates and help us understand biological mechanisms. They tell us: "In naturally immune people, antibody level X associates with protection."

**Vaccine trial frameworks** (Prentice and Qin/Gilbert) then validate whether vaccine-induced immunity follows the same rules. They test: "When a vaccine produces antibody level X, does it provide the same protection we saw in natural immunity?"

Sometimes the answer is yes, vaccine-induced antibodies work just like natural antibodies. Sometimes no, vaccine-induced immunity differs in quality, durability, or mechanism from natural immunity.

The progression typically looks like:

1. **Natural history studies:** identify that biomarker X correlates with protection
2. **Vaccine development:** design vaccines to achieve antibody level X
3. **Vaccine trials with correlate analysis:** use Prentice or Qin/Gilbert frameworks to validate that vaccine-induced antibodies at level X truly predict protection
4. **Regulatory approval:** if validated, future vaccines can be approved based on achieving antibody level X without large efficacy trials

This is why both types of correlate studies matter, even though they use different methodologies and have different limitations.

## Why This Matters Practically

These aren't just academic distinctions. When regulators decide whether to approve a new vaccine based on antibody levels instead of actual disease cases, they're relying on these statistical frameworks to determine whether those antibodies are truly mechanistic correlates or just convenient markers.

For a disease like seasonal influenza, we have a well-established correlate: a hemagglutination inhibition (HI) titer of 1:40 is commonly accepted as correlating with approximately 50% protection in adults. This has been validated across decades and multiple trials—a solid Level 2 surrogate in the Qin/Gilbert framework.

But for newer threats like COVID-19, we're still working through the hierarchy. Initial data showed neutralising antibody titres correlated with protection (CoR), then accumulated evidence suggested they could predict efficacy across variants (Level 1), and ongoing work continues to validate whether they're truly mechanistic across diverse populations (Level 2).

The terminology remains messy because immunology is complex and people use correlates of protection for different reasons. But these statistical frameworks give us rigorous tools to navigate from correlation toward causation, even when the biology refuses to be simple. From Jenner's empirical cowpox experiments to today's sophisticated statistical validation, we've come remarkably far in understanding not just *that* vaccines work, but *how* we can predict and prove their protection.

**FURTHER READING:**

Correlates of vaccine-induced protection: methods and implications, *WHO,* https://iris.who.int/server/api/core/bitstreams/7445a2ff-6b4a-415b-b127-1efb137316e0/content

Prentice, R.L. (1989), Surrogate endpoints in clinical trials: Definition and operational criteria. Statist. Med., 8: 431-440. https://doi.org/10.1002/sim.4780080407

Li Qin, Peter B. Gilbert, Lawrence Corey, M. Juliana McElrath, Steven G. Self, A Framework for Assessing Immunological Correlates of Protection in Vaccine Trials, *The Journal of Infectious Diseases*, Volume 196, Issue 9, 1 November 2007, Pages 1304–1312, https://doi.org/10.1086/522428

Callegaro, Andrea, Tibaldi, Fabian and Follmann, Dean. "Principal surrogates in context of high vaccine efficacy" *Statistical Communications in Infectious Diseases*, vol. 13, no. 1, 2021, pp. 20200003. https://doi.org/10.1515/scid-2020-0003

Gray G, Buchbinder S, Duerr A. Overview of STEP and Phambili trial results: two phase IIb test-of-concept studies investigating the efficacy of MRK adenovirus type 5 gag/pol/nef subtype B HIV vaccine. Curr Opin HIV AIDS. 2010 Sep;5(5):357-61. doi: 10.1097/COH.0b013e32833d2d2b. PMID: 20978374; PMCID: PMC2995949.

---
