---
title: "A DUMMIES' GUIDE TO SEROLOGICAL ASSAYS"
subtitle: "Not all test results mean the same thing. The trick is knowing which oracle to trust."
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
- Research
date: "2025-09-15T00:00:00Z"
lastmod: "2025-09-15T00:00:00Z"
featured: false
draft: false
---

 
{{< figure src="assay_tarot.png" alt="ASSAY Tarot Card" width="300" class="float-left" caption="A single drop of blood holds many stories—assays are how we listen." >}}

Your lab collaborator sends you a spreadsheet of data with columns labelled "ELISA_OD," "PRNT50," "HI_titre," and "PVNT_ID50." You know this has something to do with how many antibodies are in a sample, but what do these numbers actually mean? Which ones can you trust? And how is it that the same sample can tell a different story depending on which assay you look at? The key to answering these questions is understanding serological assays. 

Antibodies are the immune system’s receipts and provide molecular evidence that your body has seen an infection or a vaccine. To read those receipts, we use assays: lab tests that tell us whether antibodies are present and, sometimes, what they can do.

However, different assay readouts (often reported as titres) aren’t interchangeable. Some are quick and cheap but blunt; others are slower, pricier, and more precise. All have blind spots. Think of types of cameras: a blurry snapshot, a sharp portrait, an action shot.

When I started working with serological data, the alphabet soup of assay names was overwhelming. It took embarrassingly long to figure out which readouts to trust and when. Here is a brief summary to help avoid confusion.

---

## BINDING ASSAYS, "ARE ANTIBODIES THERE"

Binding assays ask the question: *"Do your antibodies stick to a specific viral protein?"*

**Common types of binding assays:** include ELISA (enzyme-linked immunosorbent assay), CLIA/ECLIA (chemi/electro-chemiluminescent immunoassays), Luminex, MSD platforms.

How they work ([see this video](https://www.youtube.com/watch?v=ERk0hwqhyDw)):


* First, we stick a viral protein (like spike or flu HA) onto a plastic plate or tiny beads.
* We add a diluted blood sample. If it contains antibodies that recognise that protein, they stick to it.
* We wash off anything that didn’t stick.
* We then add a second “tag” antibody that recognises human IgG or IgA (you choose which isotype you want to measure). 
* This tag carries either a color-changing enzyme or a little light maker.
* The more antibodies were stuck, the stronger the colour or light signal (often referred to as Optical Density (OD)) we see.

{{< figure src="binding_assay.png" alt="Binding assays" width="300" class="float-right" caption="" style="margin: 0 0 0rem 0rem;" >}}


### Cautionary points
**Binding ≠ protection**. This is the cardinal sin of serology interpretation. High-binding antibodies might be utterly useless against infection. It's like having a garage full of broken tools—impressive quantity, zero functionality.

For binding assays the devil's in the details, so it’s important to get a clear idea of:

* Which viral protein are we sticking to? Spike, nucleocapsid, and RBD proteins tell different stories

* Which antibody type is binding? [IgG, IgM, and IgA have different meanings and timings](https://www.youtube.com/watch?v=EcuY1uXgvqU).

* Hit the limits? Check if some samples have hit the floors/ceilings of the assay. Ignoring this will mess with your inference.

* Cross-lab comparisons? Raw numbers from different labs are like comparing currencies without exchange rates

In modern labs, high-throughput binding assays often use bead- or plate-based platforms such as Luminex or MSD, which allow researchers to measure responses to dozens of viral proteins from a single tiny blood sample.

---

## NEUTRALISATION ASSAYS, "DO ANTIBODIES WORK?"

The question: Can your antibodies prevent the virus from infecting cells? 

This is where things get serious. Neutralisation assays don't just ask if antibodies are present, they ask if they're any good at their job. It's the difference between having a security guard and having a security guard who actually stops intruders.
The output: Neutralization titre (ID50, NT50, MN50)—the dilution that cuts infection by 50%. Higher numbers = stronger protection.

{{< figure src="neut_assay.png" alt="Neut assays" width="300" class="float-left" caption="" >}}

### THREE FLAVOURS
### a) Live-virus (PRNT/FRNT) — “gold standard”

[This is a full dress rehearsal for your antibodies](https://www.youtube.com/watch?v=Up4NpJL02i8). Scientists mix a real, infectious virus with a blood sample and pour the mix onto living cells. If the antibodies work, fewer cells get infected. In the classic versions—PRNT and FRNT—you count the little marks of infection (plaques or foci) or stain for viral proteins to see what slipped through.
Pros: Most biologically relevant results you can get Cons: Slow, expensive, needs high-security labs, sensitive to every tiny protocol change

### b) Microneutralisation (MNT) — miniaturised live-virus
Same biology as live virus, just miniaturized and automated. Robots and plate readers help spot infection by changes in cell health, by staining viral proteins, or by taking images. They are great for large cohort studies where you need biological relevance but also throughput

### c) Pseudovirus neutralisation (PVNT) — “pseudo-neuts”
Uses harmless decoy viruses wearing the real virus's entry protein. Like training with rubber bullets—safer and more flexible, but not quite the real thing.
Pros: Testing new variants (just swap the spike protein) and working in regular labs Cons: Only tests the front door and misses antibodies that work after virus entry

When reporting titre values, *higher titres usually mean better protection*. But "usually" is doing heavy lifting here. Different assay formats give different absolute numbers. A pseudovirus ID50 of 1000 isn't the same as a live virus ID50 of 1000. Also try to focus on *fold-changes*, not absolute values. If variant A reduces or drops your titre 5-fold compared to the original strain, that's meaningful regardless of which assay you use.

---

## HEMAGGLUTINATION INHIBITION (HI): "THE FLU SPECIALIST

{{< figure src="HAI.png" alt="HAI assays" width="300" class="float-left" caption="Clumping of red blood cells = antibodies present!" >}}

The question: *Can your antibodies stop flu from clumping red blood cells?*

This is influenza's signature test, exploiting a quirky flu party trick: the virus naturally makes red blood cells stick together like magnetic beads.

**How it works*:*
Mix virus + red blood cells + serum in dilutions, then look:

* Antibodies work: Cells form a tight button (no clumping)
* Antibodies fail: Cells spread in a fuzzy mat (clumping wins)
Find the highest dilution that still prevents clumping = your HI titre.

The HI assay has endured because it is a wonderfully low-tech and time-tested method. No fancy equipment, no biosafety concerns, and you get results in hours. It's the Swiss Army knife of flu surveillance.

*The Catch:* Mainly used for flu, though it can be applied to other viruses that hemagglutinate (e.g. historically measles, parainfluenza). It's picky about protocol details; different types of red blood cells can affect your numbers.


---

## Rapid Tests: "The Quick Check"

The question: *"Are antibodies detectable right now?"*

Think pregnancy test for immunity. Blood wicks along a strip, line appears if antibodies are there. This is perfect for field studies, point-of-care screening, "do I have any immunity?" questions.

Terrible for: Quantifying levels, predicting protection, or rigorous immulogical research.

---

## CHEAT SHEETS FOR SEROLOGICAL ASSAYS 

### Research questions:

- *"Has this population been exposed?"* → Binding assays (multiplex if you can swing it)
- *"Are people protected?"* → Neutralization assays (live virus for accuracy, pseudovirus for variants)
- *"How well did the flu vaccine work?"* → HI assays
- *"Quick field screening?"* → Rapid tests (with major caveats)

### Data handling tips:
- Always use log scales (antibody data is naturally log-normal)
- Don't ignore detection limits (use proper censored data methods)
- Account for batch effects if you can (they're everywhere in lab data)
- Standardise across labs (or accept you're comparing apples to oranges)


### Common traps
- The *binding = protection fallacy*: Just because antibodies bind doesn't mean they protect. Always check if you have functional data.
- The *bigger-is-better assumption*: Higher neutralising titres usually mean good immunity, but saturation and antibody ceiling effects can create weird non-linear relationships.
- The *data-mixing temptation*: Don't pool different assay types without proper calibration. They're measuring related but different things.

### What to ask my lab partners
- What exactly was measured and how?
- How many samples hit detection limits?
- What standards were used?
- Any batch effects or protocol changes?

These questions can save you months of analytical headaches.

## THE BOTTOM LINE

Serological assays are like different types of witnesses in a court case. Each tells part of the story, each has biases, and none gives you the complete picture alone. Binding assays show you population exposure patterns. Neutralization assays reveal functional immunity. Specialized assays like HI give pathogen-specific insights.
The trick isn't finding the "perfect" assay, it's understanding what each one can and can't tell you, then using them together intelligently.

Remember: the same blood sample can give wildly different numbers depending on which test you use. That's not a bug, it's a feature. Each assay captures a different slice of the immune response. Your job is to know which slice you're looking at and what it means for your research question.

*Pro tip*: There are many other types of assays not mentioned here; when encountering a new assay type, spend 15 minutes understanding the underlying biology. It'll save you weeks of confusion when the results don't behave as expected.


---