<p align="center"> <img src="https://raw.githubusercontent.com/annehulsey/TURtLES/main/doc_src/figures/TURtLES_title.PNG" align="middle" height=75 /></p>

<p align="center"> <b>T</b>he <b>U</b>ncertainty in <b>R</b>egional-<b>L</b>evel <b>E</b>arthquake <b>S</b>cenario simulation </p>




## What is it?

`TURtLES` is a Python package that provides tools for simulating a set of regional ground motion maps that represent a selected earthquake scenario, based on the uncertainty associated with a ground motion model (GMM).

## What can I use it for?

`TURtLES` generates a set of simulated ground motion maps that represent the potential range of ground shaking intensities associated with a earthquake scenario. For example, the spectral accelerations, Sa(T), experienced across downtown San Francisco during a magnitude 7.2 event on a nearby segment of the San Andreas Fault.

These sets of ground motion maps are typically utilized in regional performance assessments that consider the range of potential performance, as opposed to the expected performance. These assessments include uncertainty in both the ground shaking intensity and the built environment's response to the shaking.

## How does it work?

`TURtLES` first uses SimCenter's [EQHazard tool](https://github.com/NHERI-SimCenter/GroundMotionUtilities/tree/master/EQHazard) to input a selected earthquake scenario (a rupture magnitude and location) and extract ground motion predictions (medians and standard deviations) for spatially distributed site locations. See the [EQHazard documentation](https://github.com/NHERI-SimCenter/GroundMotionUtilities/tree/master/EQHazard) for details on the available earthquake forecast rupture (ERF) models and ground motion models (GMMs). The EQHazard version included in the package was built on May 7, 2021.

`TURtLES` then uses a computationally efficient model ([Markhvida et al. 2018](https://doi.org/10.1002/eqe.3007)) for simulating spatially correlated residuals across multiple periods. The simulated residuals are combined with the medians and standard deviations at each site location. See [Markhvida et al. 2018](https://doi.org/10.1002/eqe.3007) for more details. (Note that this correlation model only considers periods up to 5 seconds. In order to include periods greater than 5 seconds, `TURtLES` assumes perfect correlation among the residuals for periods between 5 and 10 seconds.)

## How can I get started?

You can get oriented with [two examples](https://github.com/annehulsey/TURtLES/tree/main/example) provided as Jupyter Notebooks on the `TURtLES` GitHub repository. 
- ***Selecting a Rupture Scenario***: uses the EQHazard tool to filter an ERF's ruptures to identify a relevant source and rupture index for the desired magnitude and location (a M<sub>w</sub>7.2 on the San Andreas Fault). 
- ***Simulate Ground Motion Maps for a Rupture Scenario***: generates a set of simulated ground motion maps for the earthquake scenario, based on the site locations and the elected GMM (Chiou and Youngs, 2014).

## Installation

`TURtLES` is available at the Python Package Index (PyPI). You can simply install it using `pip` as follows:

```
pip install TURtLES
```

## Licence

`TURtLES` is distributed under the MIT license, see [LICENSE](https://github.com/annehulsey/TURtLES/blob/main/LICENSE).

## Contact

Anne Hulsey, University of Auckland, anne.hulsey@auckland.ac.nz

