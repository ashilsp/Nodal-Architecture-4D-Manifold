# The Nodal Architecture of the 4D Manifold

### The Manifold Saturation Principle and the Topological Origin of Galactic Scaling Laws

This repository contains the computational framework, numerical engine source code, and validation scripts for the manuscript **"The Nodal Architecture of the 4D Manifold: The Manifold Saturation Principle and the Topological Origin of Galactic Scaling Laws"**.

---

## 1. Primary Theoretical Foundations

This computational framework models the conversion of 3D baryonic configurations into stable 4D manifolds across three distinct scaling domains:

1. **The Manifold Saturation Principle ($S_M$):** Tracks critical mass density limits at the $R_d$ interface layer:
   $$S_M = \frac{D \cdot \Phi_{\text{curvature}}}{\epsilon_M}$$
2. **Manifold Viscosity Integration ($\eta_M$):** Resolves the galactic winding paradox and stabilizes spiral arms natively via a viscous coupling diffusion field:
   $$\frac{d\mathbf{v}}{dt} = -\nabla \Phi_{\text{grav}} + \nu_M \nabla^2 \mathbf{v}$$
3. **Topological Torque Parity ($\tau_M$):** Establishes the 2/3 macro-scale spin orientation bias through a global bulk shear field acting on node ignition thresholds:
   $$\Delta E_{\text{prograde}} < \Delta E_{\text{retrograde}}$$

---

## 2. Current Repository Structure

The current codebase contains the core physics solvers and plotting tools mapping to the main manuscript text:

```text
├── README.md                  <- This repository directory guide
├── requirements.txt           <- Environment software dependencies
├── src/                       <- Core mathematical physics calculators
│   ├── saturation.py          <- Original mass-gap threshold solver
│   ├── manifold_viscosity.py  <- Viscous space-stiffening & equation of motion solver
│   └── global_shear_parity.py <- Monte Carlo distribution engine for cosmic parity fields
└── scripts/                   <- Automated verification plots
    ├── generate_fig2.py       <- Original evolutionary density plotting tool
    ├── generate_rotation_curves.py  <- Generates flat galactic velocity profiles
    └── generate_parity_plots.py     <- Plots filament alignment profiles vs. void isotropy
