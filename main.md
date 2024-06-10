---
title: "Encyclopedia chapter about resuspension"
output: pdf_document
bibliography: references.bib
---

# Numerical modelling

Operational forecast systems typically rely on volcanic ash transport and dispersal (VATD) models to produce quantitative forecasting products. VATD models allow to simulate the atmospheric transport of ash released from a volcanic source using a physics-based approach. In addition, VATD models can be used to simulate the main processes involved in the life cycle of resuspended ash: emission, atmospheric transport and ground re-deposition. However, the traditional source term definition used for volcanic eruptions in VATD models must be reformulated to enable ash resuspension modelling. To this purpose, both Lagrangian and Eulerian dispersion models (e.g., NAME, HYSPLIT and FALL3D) have been adapted to simulate the transport of ash resuspended clouds by incorporating new emission schemes. As opposed to a single point source or a vertical line of sources needed by VATD models to describe eruptive columns, ash resuspension requires a continuum of sources distributed over a region with tephra fallout deposits. Moreover, the emission sources are unknown in advance as they are dynamically activated or deactivated depending on varying meteorological and land-surface conditions. In consequence, VATD models must be coupled with Numerical Weather Prediction (NWP) models and Land-Surface Models (LSMs) to properly parametrise the emission threshold and the spatiotemporal variability of the emission fluxes.

During the last decade, most of the studies on numerical modelling of volcanic ash resuspension have parameterised the emission source term using simple dust emission schemes. Since the mobilisation of soil particles due to the wind influence depends on the transfer of momentum from the atmosphere to a rough ground surface, dust emission schemes have customarily expressed the emission rate in terms of the surface Reynold's stress:
$$ \tau = \rho_a u_*^2 $$
where $\rho_a$ is the air density and $u_*$ is the so-called friction velocity. Dust emission is a nonlinear process and experimental studies and semi-empirical models have shown that the vertical emission flux can be expressed as 
$$ F_v \sim u_*^n $$
in the limit $u_* \gg u_{*t}$ with the exponent ranging between 2 and 5, approximately. Additionally, an expression for the threshold must be provided to ensure a closed system of equations.

In the limit of large particle, the threshold velocity can be computed using the classical expression derived by 
$$ u_{*t} \propto \sqrt{ \dfrac{\rho_p}{\rho} d } $$
being $\rho_p$ the particle density, $rho_a$ the air density and $d$ is the grain size.


# Basura
Realistic forecasting of ash clouds requires robust meteorological and source-term data. Online VATD models are coupled with Numerical Weather Prediction (NWP) models according to an integrated modelling system that enables a two-way data exchange of data. However, online modelling systems are extremely demanding in terms of computational resources because of the complexity of NWP models, which can be a significant limitation for operational systems. Alternatively, some VATD models are run separately following an offline approach and allow exclusively a one-way coupling of the meteorology. The offline coupling has low computational cost since VATD models can benefit from already available meteorological data provided by weather agencies. This approach is particularly well-suited to early warning systems with urgent computing needs whenever the response time is critical once an eruption has started. As a counterpart, the online approach represents the atmospheric processes more realistically and errors introduced by the offline approach can be significant in some cases. 




# Satellite
When remote-sensing data and observations from the ground
and aircraft are available, these model predictions can be
compared and validated. Before, and in the initial stages of
volcanic eruptions, VATD models are invaluable in predicting
the movement of volcanic ash clouds and ensuring aviation
safety.

* copiado 

# References

