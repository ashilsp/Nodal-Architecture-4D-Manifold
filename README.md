# The Nodal Architecture of the 4D Manifold
### The Manifold Saturation Principle and the Topological Origin of Galactic Scaling Laws

This repository contains the computational framework, numerical proofs, and supplementary simulations for the paper "The Nodal Architecture of the 4D Manifold."

## 1. Overview: The Manifold Saturation Principle ($S_M$)
This project demonstrates the transition of baryonic matter into a 4D nodal state at the $R_d$ interface. We introduce the **Manifold Saturation Principle** as a diagnostic law for spacetime stability:

$$S_M = \frac{D \cdot \Phi_{curvature}}{\epsilon_M}$$

Where:
- **$D$**: Localized mass-density.
- **$\Phi$**: Geometric curvature.
- **$\epsilon_M$**: Intrinsic manifold elasticity.

## 2. Repository Structure
- `/src`: Core Python implementation of the OCM Hamiltonian and $S_M$ metric.
- `/scripts`: Tools for calculating the Density Ceiling ($\rho_{crit}$) and avoiding singularities.
- `/notebooks`: Verification scripts for the Tully-Fisher $v^4 \propto M$ derivation.
- `/media`: Supplementary high-speed visual simulations ($S_1$–$S_{20}$).

## 3. Supplementary Media: $S_1$ to $S_{20}$
The videos in the `/media` directory provide visual evidence of the **Order Creator Mechanism (OCM)** during nodal ignition.

* **$S_1$–$S_5$**: Initial manifold tension and the onset of the metastable bottleneck.
* **$S_6$–$S_{12}$**: Critical Saturation ($S_M \approx 1.0$) showing the formation of the "Hollow Core" and the 4D bridge; includes super-critical events ($S_M > 2.0$) simulating Kilonova splicing and high-energy manifold stiffening.
* **$S_{13}$–$S_{20}$**: Large-scale tethering and global shear dynamics that govern galactic evolution and cosmological isotropy.


## 4. Computational Proof: Tully-Fisher Scaling
To verify the topological origin of galactic scaling laws, run the provided proof script. This script uses the Manifold Saturation constant ($a_0 \approx 1.2 \times 10^{-10} m/s^2$) to recover the flat rotation curve scaling.

### Instructions:
1. Ensure you have the requirements installed:
   `pip install -r requirements.txt`
2. Run the proof:
   `python notebooks/Tully_Fisher_Proof.py`

The output will confirm the $v^4 \propto M$ relationship derived from manifold viscosity rather than dark matter particles.

---
**Author:** Ashil S.  
**Contact:** ashilsp@gmail.com
