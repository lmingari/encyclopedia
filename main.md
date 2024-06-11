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
in the limit $u_* \gg u_{*t}$ with the exponent ranging between 2 and 5, approximately. 

Additionally, an expression for the threshold must be provided to ensure a closed system of equations. In the limit of large particles, the wind erosion threshold friction velocity can be computed using the well-known expression derived by @bagnold1941: 
$$ u_{*t}^2 \propto \sigma_p g d $$
being $\sigma_p=\rho_p/\rho_a$ the particle-to-air density ratio, $g$ the acceleration of gravity and $d$ is the grain size. However, for small particles $u_{*t}$ increases rapidly with decreasing $d$ and this expression is not valid since it does not take into account the effect of interparticle cohesive forces. @shao2000 derived a more realistic expression for spherical particles loosely spread over a dry and bare surface which can be applied to multiple grain sizes:
$$ u_{*ts}^2 \propto \sigma_p g d + \dfrac{\gamma}{\rho_a d} $$
This expression depends on an experimental parameter $\gamma$ and has been extensively used in numerical models (Fig. 1). According to some numerical studies, a well-suited value of $\gamma$ for fresh volcanic deposits is around $\gamma \sim 1.65 \times 10^{-4}~kg~s^{-2}$, while $\gamma \gtrsim 3 \times 10^{-4}~kg~s^{-2}$ is a reasonable assumption for ancient deposits.

The expression of $u_{*ts}$ for idealised bare and dry soils needs to be corrected taking into account multiple factors, including soil moisture and the influence of nonerodible surface roughness elements. The general expression
$$ u_{*t} = u_{*ts} f(w,\lambda,\dots) $$
provides a simple approach to evaluate the threshold friction velocity for natural surfaces using a correction function ($f>1$) accounting for the increase of the threshold due to the influence of soil moisture ($w$), the density of surface-roughness elements ($\lambda$), among other factors.

A realistic representation of the spatial distribution of emission sources for ash resuspension requires robust weather and land-surface data. The NWP model provides the atmospheric variables needed by the emission scheme, including air density and friction velocity. Specifically, the friction velocity can be computed by the surface layer scheme included within the NWP model or estimated from the wind profile or even from the surface wind using empirical parameterisations. On the other hand, the land-surface model provides critical information required to estimate the erosion threshold, such as volumetric or gravimetric soil moisture, roughness length or vegetation cover fraction, etc... Typically, NWP models include a LSM to represent land processes and provide heat and moisture fluxes over land surface to the parent atmospheric model. However, the land-surface information provided by most of the available regional NWP models and global datasets (e.g., ERA5 reanalysis or GFS) is not representative of the land-surface conditions and spatial scales involved in the ash emission process. In addition, the LSM does not generally include information related to the tephra fallout deposit and, consequently, is the weakest link in the ash resuspension modelling system as an ad hoc land-surface model is required to obtain crucial information for the ash emission scheme.

![Figure 1: Threshold friction velocity according to the expression derived by @shao2000 for soils with uniform and spherical particles spread loosely over a dry and bare surface. Under this ideal condition, the threshold can be expressed as a function of only particle size. As an example, the figure shows some typical values of the experimental parameter $\gamma$ considered in numerical studies of ash resuspension.](scripts/ust_th.png)

# References

