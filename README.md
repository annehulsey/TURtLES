# TURtLES
**T**he **U**ncertainty in **R**egional-**L**evel **E**arthquake **S**cenario simulation



This package simulates regional ground motion maps for a selected earthquake scenario, based on the uncertainty associated with a ground motion model (GMM).

The ground motion model is implemented for the selected rupture and site locations via SimCenter's [EQHazard tool](https://github.com/NHERI-SimCenter/GroundMotionUtilities/tree/master/EQHazard). See the link for details on the available earthquake rupture forecast (ERF) models and GMMs. The outputs of the tool are medians and standard deviations at each site location. The EQHazard version included in the package was built on May 7, 2021.

Each simulated ground motion map realization includes spatial correlation across multiple periods. The correlations are generated via the computationally efficient method developed by [Markhvida et al. (2018)](https://doi.org/10.1002/eqe.3007). (Note that this model only considers periods up to 5 seconds. In order to include periods greater than 5 seconds, this package assumes perfect correlation among the residuals for periods between 5 and 10 seconds.)

The Example folder includes two Jupyter Notebooks to orient the user. *Selecting a Rupture Scenario* identifies an ERF's ruptures and filters them to identify a relevant source and rupture index for the desired location and magnitude. *Simulate Ground Motion Maps for a Rupture Scenario* generates a set of realizations based on the selected indices and ground motion model.

