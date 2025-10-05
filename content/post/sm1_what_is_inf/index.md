---
title: 'WHAT DOES IT MEAN TO BE INFECTED?'
subtitle: 'Unpacking the blurred lines between biology, diagnosis, transmission, and immunity'
summary: ''
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
date: "2025-09-15T00:00:00Z"
lastmod: "2025-09-15T00:00:00Z"
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: 
- imm_sero

# Set captions for image gallery.
gallery_item: []
---
 
{{< figure src="infection_tarot.png" alt="Infection Tarot Card" width="300" class="float-left" caption="Defining infection is like reading tarot cards - the interpretation depends on who's asking and what they're looking for." >}}

You wake up with a sore throat. You take a lateral flow test, negative. The next day, still negative. A PCR comes back "positive". Meanwhile, your flatmate tested positive on a rapid test but felt fine throughout.

So who was infected? You, your friend, both, or neither?

It sounds simple, but defining someone as “infected” is not as clear-cut as it first appears. Infection is a biological process, but it is also a clinical judgement, an epidemiological state, and an immunological inference. Which one matters depends on who’s asking and why.

## THE TRADITIONAL DEFINITION

[Wikipedia](https://en.wikipedia.org/wiki/Infection), everyone’s favourite textbook, defines infection with something tidy:

*“Infection is the invasion of tissues by pathogens, their multiplication, and the reaction of host tissues to the infectious agent and the toxins they produce.”*

On the surface, this seems clear: a pathogen enters a host, starts multiplying, and the host responds.
The process typically unfolds in four stages:

&nbsp;&nbsp;&nbsp;&nbsp;1. Exposure: a pathogen enters via the nose, gut, skin, or another route.

&nbsp;&nbsp;&nbsp;&nbsp;2. Entry and replication: many are destroyed immediately, but some succeed in infecting cells.

&nbsp;&nbsp;&nbsp;&nbsp;3. Evasion and spread: if replication outpaces early immune defences, the pathogen expands.

&nbsp;&nbsp;&nbsp;&nbsp;4. Host response: symptoms arise both from the pathogen itself and from the immune system's attempts to control it.
 
But even this leaves questions. Do we call “infection” the moment the first viral particle sneaks in? How about when replication has taken off? Or only once the host shows symptoms? The traditional definition is helpful, but it leaves blurry edges. Philosophers call this the [Sorites Paradox](https://www.youtube.com/watch?v=y-jexokX3Gk&t=73s). Think about what point a person becomes bald (something I think about a lot in my 30s…). Balding is a continuous process, but baldness as a binary concept is open to interpretation. Infection is a similar continuum, but based on levels of particles, replication, symptoms, shedding, and antibodies instead of precious hair.

## INFECTION AS A FUZZY CONCEPT IN EPIDEMIOLOGY

Unlike a broken bone, which shows up clean on an X-ray, infection doesn’t come with a crisp signature. There are three main ways researchers define infection:

* Symptom profiles: which are specific to a pathogen
* PCR testing: which detects genetic fragments of the virus
* Antibodies change: analysed blood samples show how the immune system responded

When we conduct big [epidemiological cohort studies](https://pmc.ncbi.nlm.nih.gov/articles/PMC9536647/), we are often interested in answering: how many people are infected? But even this simple question can be murky to answer. Often, cohort studies rely on i) self-reporting of symptoms, ii) PCR testing (virological), and iii) testing blood samples for antibodies (serological). Using all or a subset of these metrics, we establish a pre-emptive "infection case" definition. E.g. when considering PCR, we might consider a single positive sample as “infected”, for bloods, we often use a “four-fold rise” in antibody titre to indicate an infection event. That’s convenient but arbitrary, and it hides the complexities of biology.

## KNOWING WHAT WE CAN’T SEE

Even if we agree on a definition of infection, we face the problem of how we know.
All our tools are imperfect windows:

* PCRs can miss the virus if the swab doesn’t catch it, and the fragments detected may be harmless leftovers.
* Antibody titres fluctuate naturally, and they appear late relative to symptoms, and sometimes not at all.
* Symptoms often overlap with many other illnesses, particularly for respiratory viruses, and some people never have them.

Because these are ultimately imperfect tools, statisticians would say infection is a latent variable, a hidden state. We never observe it directly; we infer it from noisy signals. That’s not just a technical challenge but a philosophical one: we’re reasoning about something real, but always indirectly.

{{< figure src="figure_latent.png" alt="Latent Variable Model" width="700" class="float-right" caption="Infection as a latent variable - we never observe it directly, but infer it from noisy signals like PCR tests, symptoms, and antibody responses." >}}


## COHORT STUDIES AND THE IMMUNOLOGICAL LENS

Zoom out to long-term cohort studies, and the challenge deepens. I often work with datasets with only a few blood draws per year, and limited PCR-testing capacity, and infections must be inferred. If antibodies rise, we assume infection. But:

* Some infections barely nudge titres.
* Some rises are noise or cross-reactivity.
* Vaccination can look identical to infection.

This matters for host kinetics (how antibodies rise and fade). If infections are misclassified, estimates of kinetics are distorted.

It also matters for correlates of protection (CoP), the holy grail of vaccine research. To say “an antibody level of X protects against infection,” we need to know who was infected. If infection inference is shaky, CoP estimates are shaky too.

Take influenza: people with strong baseline immunity may not show much of an antibody rise even when infected. If we label them “uninfected,” we underestimate how protective their antibodies really were.

## AUDIENCE AND CONTEXT MATTER

Different collaborators often carry their own default ideas of what “infection” means:

*	Clinicians: does this patient need a diagnosis or treatment?
*	Transmission modellers: is this person contributing to the spread?
*	Immunologists: did this exposure boost immunity?
*	Policy makers: how many cases should we count?
*	Public health: how much disease burden are we preventing?

I’ve found it’s best to be upfront and explicit about definitions. That means being clear about what we’re treating as the endpoint and about the method for inferring infection (PCR, serology, clinical diagnosis, or combinations). Stating this at the outset helps avoid confusion — especially in talks or interdisciplinary projects where each audience may default to a different meaning.

## FINAL THOUGHTS

Infection is not a neat binary but a spectrum: exposure, replication, symptoms, shedding, and antibodies. What counts as “infected” depends on whether you care about biology, transmission, immunity, or disease reduction.

To ask “am I infected?” or “how many infections did this vaccine prevent?” is really to ask a bundle of different questions. The answers matter, not just for personal reassurance, but for how we measure immunity, design studies, and protect communities.

Perhaps infection is best seen not as a single state but as overlapping stories: clinical, epidemiological, immunological. Each is partial, each is useful, and together they shape how we live with pathogens.

---
