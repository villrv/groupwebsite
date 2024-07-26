---
title: "Research"
layout: default
excerpt: "RT2 Lab -- Research"
sitemap: false
permalink: /research/
---

# Research

Our group studies *time-domain astrophysics*--dynamic "bumps in the night" across the Cosmos. We use a combintation of observations, theory and data-driven methodologies to study the eruptions, explosions and collisions of stars. We are interested in understanding fundamental questions of our universe, including: How do massive stars end their lives? What can the most exotic stellar explosions teach us about high-energy astrophysics? Where (and when) are the heaviest elements made? 

## Machine Learning Methods for Time-domain Astrophysics

<img src="/images/zoo.png#right" alt="drawing" width="400"/>


*Thousands* of transients--including the eruptions, explosions and collisions of stars--are discovered annually. Any in just a few years, the Vera C. Rubin Observatory will come online and increase this discovery rate to *millions* annually.

Our team develops novel methodologies to:

 - Classify supernovae and other transient events. There exists a zoo of supernova types, which are traditionally classified via spectroscopy. Given the immense discovery rate of these events, modern surveys classify transients using their *light curves*, or light as a function of time and wavelength. We develop methods to rapidly classify these events using the rich data provided by wide-field surveys.
 - Identify rare physics. Given the *millions* of transients the Rubin Observatory is expected to discover, it is not unreasonable for us to expect something *never-before-seen* in the data! Our group develops physics-agnostic approaches to finding rare physics in realtime. 
 - Infer the underlying properties of Cosmic explosions. Given the millions of discoveries, you wouldn't be surprised to hear that extracting physical information from our data can be quite expensive! We develop novel techniques to rapidly speed up (and low the cost!) of physical inference for extragalactic transients.

 Some relevant papers from our group:

- Wang et al. (2023), [SBI++: Flexible, Ultra-fast Likelihood-free Inference Customized for Astronomical Applications
](https://iopscience.iop.org/article/10.3847/2041-8213/ace361/meta)
- Chan et al. (2022), [Searching for Anomalies in the ZTF Catalog of Periodic Variable Stars](https://iopscience.iop.org/article/10.3847/1538-4357/ac69d4/meta)
- Villar (2022), [Amortized Bayesian Inference for Supernovae in the Era of the Vera Rubin Observatory Using Normalizing Flows
](https://arxiv.org/abs/2211.04480)
- Villar et al. (2021), [A Deep-learning Approach for Live Anomaly Detection of Extragalactic Transients
](https://iopscience.iop.org/article/10.3847/1538-4365/ac0893/meta)
-  Villar et al. (2020), [SuperRAENN: A Semisupervised Supernova Photometric Classification Pipeline Trained on Pan-STARRS1 Medium-Deep Survey Supernovae](https://iopscience.iop.org/article/10.3847/1538-4357/abc6fd/meta)


## Observational Studies of Supernovae and Other Transients

<img src="/images/ps1.jpeg#left" alt="image of Pan-STARRS" width="400">


After discovery and initial classification, our group uses a variety of ground- and space-based observatories to understand the physics driving astrophysical transients. We are particularly interested in core-collapse supernovae, especially those of exotic progenitor systems. Such events are direct tests of massive stellar evolution (e.g., for eruptive mass-loss models driven by unstable nucleosynthesis) and binary interactions.

We are members of the [Young Supernova Experiment](https://yse.ucsc.edu/) (YSE), a ~1500 square degree survey conducted with the Pan-STARRS telescopes that aims to discover young and rare events in the northern sky. To date, YSE has discovered thousands of supernovae, tidal-disruption events and other transients.

 Some relevant papers from our group:

- Ransome et al. (2023), [SN2023ixf in Messier 101: the twilight years of the progenitor as seen by Pan-STARRS
](https://arxiv.org/abs/2312.04426)
 - Yadavalli et al. (2023), [SN 2022oqm: A Multi-peaked Calcium-rich Transient from a White Dwarf Binary Progenitor System
](https://arxiv.org/abs/2308.12991)
- Aleo et al. (2023) [The Young Supernova Experiment Data Release 1 (YSE DR1): Light Curves and Photometric Classification of 1975 Supernovae
](https://iopscience.iop.org/article/10.3847/1538-4365/acbfba/meta)
- Villar et al. (2018) [Spitzer Space Telescope Infrared Observations of the Binary Neutron Star Merger GW170817](https://iopscience.iop.org/article/10.3847/2041-8213/aad281/meta)
- Villar et al. (2016) [The intermediate luminosity optical transient sn 2010da: The progenitor, eruption, and aftermath of a peculiar supergiant high-mass x-ray binary](https://iopscience.iop.org/article/10.3847/0004-637X/830/1/11/meta)


## Multimessenger Astrophysics and the Origin of Heavy Elements

<img src="/images/knlc.jpeg#right" alt="image of Pan-STARRS" width="400">


The heaviest elements in our universe (i.e., those arising from the rapid neutron-capture process) are produced primarily in the collisions of neutron stars. However, alternative sites of such nucleosynthsis have been proposed, such as the deaths of rapidly rotating stars. Our group:

-  Designs follow up strategies for mergers detected via gravitational wave detectors. The electromagnetic emission accompanied by gravitational waves is a ``smoking gun'' signature for the recent formation of heavy elements, such as gold and platinum. 
- Uses ultraviolet, optical and near infrared data to understand the detailed physics of *kilonovae*, the electromagnetic counterpart to binary neutron star mergers. Multi-wavelength observations of these events can be used, in conjunction with gravitatoinal waves, to understand the nature of neutron star mergers. 
- Searches for alternative sites of r-process nucleosynthesis. The collapse of rapidly spinning, massive stars has been suggested as a viable secondary origin of heavy elements. Our group conducts detailed studies of such sites to directly constrain this possibility.


 Some relevant papers from our group:
- Blanchard et al. (2023) [JWST Observations of the Extraordinary GRB 221009A Reveal an Ordinary Supernova Without Signs of r-Process Enrichment in a Low-Metallicity Galaxy](https://arxiv.org/abs/2308.14197)
- Ristic et al. (2023) [Interpolated kilonova spectra models: Examining the effects of a phenomenological, blue component in the fitting of AT2017gfo spectra
- Villar et al. (2018) [Spitzer Space Telescope Infrared Observations of the Binary Neutron Star Merger GW170817](https://iopscience.iop.org/article/10.3847/2041-8213/aad281/meta)
- Villar et al. (2017) [The Combined Ultraviolet, Optical, and Near-infrared Light Curves of the Kilonova Associated with the Binary Neutron Star Merger GW170817: Unified Data Set, Analytic Models, and Physical Implications](https://iopscience.iop.org/article/10.3847/2041-8213/aa9c84/meta)

## Models and Tools

Our group produces a number of open-source tools and new, analytical models to understand extragalactic transients:

- [SuperRAENN](https://github.com/villrv/SuperRAENN) -- classification method for supernovae
- [Superphot+](https://github.com/VTDA-Group/superphot-plus) -- classification nmethod for supernovae
- [LIGHETR](https://github.com/VTDA-Group/LIGHETR_Alert_System0) -- alert system for gravitational waves
- [extrabol](https://github.com/villrv/extrabol) -- method to estimate the bolometric light curves of thermal transients
- [MOSFiT](https://github.com/guillochon/MOSFiT) -- an inference/modelling package for extragalactic transients
