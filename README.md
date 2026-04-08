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
- `/scripts`: Tools for calculating the Density Ceiling ($\rho_{crit}$) and generating the **Figure 2a Bifurcation plot**.
- `/notebooks`: Verification scripts for the Tully-Fisher $v^4 \propto M$ derivation.
- `/media`: Supplementary high-speed visual simulations ($S_1$–l to $S_{20}$).

## 3. Supplementary Media: $S_1$ to $S_{20}$
The videos in the `/media` directory provide visual evidence of the **Order Creator Mechanism (OCM)** during nodal ignition.

* **$S_1$ to $S_{5}$** : Initial manifold tension and the onset of the metastable bottleneck.
* **$S_6$ to $S_{12}$** : Critical Saturation ($S_M \approx 1.0$) showing the formation of the "Hollow Core" and the 4D bridge; includes super-critical events ($S_M > 2.0$) simulating Kilonova splicing and high-energy manifold stiffening.
* **$S_{13}$ to $S_{20}$** : Large-scale tethering and global shear dynamics that govern galactic evolution and cosmological isotropy.

## 4. Computational Proofs and Visualizations
To verify the topological origin of galactic scaling laws and stellar bifurcation, run the provided scripts.

### Instructions:
1. **Environment Setup**:
   `pip install -r requirements.txt`

2. **Verify Tully-Fisher Scaling ($v^4 \propto M$)**:
   `python notebooks/Tully_Fisher_Proof.py`

3. **Generate Figure 2a (Evolutionary Bifurcation)**:
   `python scripts/generate_fig2.py`

The outputs will confirm the manifold saturation thresholds and the relationship derived from manifold viscosity rather than dark matter particles.

---
**Author:** Ashil S.  
**Contact:** ashilsp@gmail.com
