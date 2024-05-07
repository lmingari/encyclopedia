---
title: "Encyclopedia chapter about resuspension"
output: pdf_document
bibliography: references.bib
---

# Numerical modelling

Operational forecast systems typically rely on volcanic ash transport and dispersal (VATD) models which play a crucial role in producing forecasting products. VATD models allow to simulate the atmospheric transport of ash released from a volcanic source using a physics-based approach.

Realistic forecasting of ash clouds requires robust meteorological and source-term data. Online VATD models are coupled with Numerical Weather Prediction (NWP) models according to an integrated modelling system that enables a two-way data exchange of data. However, online modelling systems are extremely demanding in terms of computational resources because of the complexity of NWP models, which can be a significant limitation for operational systems. Alternatively, some VATD models are run separately following an offline approach and allow exclusively a one-way coupling of the meteorology. The offline coupling has low computational cost since VATD models can benefit from already available meteorological data provided by weather agencies. This approach is particularly well-suited to early warning systems with urgent computing needs whenever the response time is critical once an eruption has started. As a counterpart, the online approach represents the atmospheric processes more realistically and errors introduced by the offline approach can be significant in some cases.

VATD models can also be used to simulate the main processes involved in the life cycle of resuspended ash: emission, atmospheric transport and ground re-deposition, and both Lagrangian and Eulerian dispersion models, including NAME, HYSPLIT and FALL3D, have been used to perform numerical simulations of ash resuspended clouds. However, the source term definition for volcanic eruptions in VATD models must be reformulated to enable ash resuspension modelling. Most models represent the volcanic source as a vertical line characterised by a vertical mass distribution and a mass eruption rate and the source location for a given vent is known in advance. As opposed to a single point source or a vertical line required for eruptive columns, ash resuspension requires a continuum of potential sources distributed over a region affected by tephra fallout deposits. Moreover, the emission sources are unknown in advance as they are dynamically activated or deactivated depending on varying weather conditions.

During the last decade, studies on numerical modelling of volcanic ash resuspension since the original works of @leadbetter2012 and @folch2014 have parameterised the source term using simple dust emission schemes.

# Satellite
When remote-sensing data and observations from the ground
and aircraft are available, these model predictions can be
compared and validated. Before, and in the initial stages of
volcanic eruptions, VATD models are invaluable in predicting
the movement of volcanic ash clouds and ensuring aviation
safety.

* copiado 

# References

