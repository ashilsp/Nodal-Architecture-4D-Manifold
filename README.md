# Quantum-Geometric Regulation & Galactic Tethering (OCM Engine)

This repository contains the official, decoupled computational validation suite for the Order Creator Mechanism (OCM) framework. The modules included here provide the rigorous numerical backing, mathematical derivations, and plotting runners verifying the non-singular metrics, thermodynamic floors, and galactic scaling relationships detailed in the main manuscript.

---

## 🛠️ Repository Architecture Map

The code is divided into a core physics mathematical library (`/src`), an automated publication plotting suite (`/scripts`), and interactive algebraic playgrounds (`/notebooks`).

### 1. Fundamental Quantum & Boundary Dynamics
* **`src/saturation.py`** | Models the Planck-Schwarzschild intersection boundary, tracking horizon puncture limits and the non-singular density ceiling ($\rho_{crit}$).
  * *Verification Runner:* `scripts/generate_fig2.py`
* **`src/quantum_regulation.py`** | Implements the modified $\kappa$-Hamiltonian potential barrier ($V_{top}$), solving the wave-packet locking profile at the $R_d$ boundary shell.
  * *Verification Runner:* `scripts/generate_quantum_plots.py`
* **`src/ocm_hamiltonian.py`** | Codifies the strict piecewise step-discontinuity potential floor ($E_0$) and evaluates energy-to-mass frequency quantization scaling.
  * *Verification Runner:* `scripts/generate_hamiltonian_plots.py`

### 2. Micro-Oscillations & Internal Thermodynamics
* **`src/quantum_nodal_dynamics.py`** | Simulates the structural resonator frequencies of the Oloid-topology, forcing the coupled poloidal and toroidal modes into the exact, immutable $3:2$ ratio. Implements the zero-accretion baseline "Ghost Pulse" proof.
  * *Verification Runner:* `scripts/generate_qpo_spectra.py`
* **`src/thermodynamics.py`** | Evaluates the hybrid active/dormant quasar profile ($L_{obs} = \eta \dot{M} c^2 + \Lambda_{OCM}$), establishing the 50,000x radiative excess floor and non-thermal QGP topological hardening.
  * *Verification Runner:* `scripts/generate_luminosity_floor.py`
* **`src/forensics.py`** | Models the "Big Blue Bump" ultraviolet excess profiles and calculates cross-regime Doppler geometric frequency scaling.
  * *Verification Runner:* `scripts/generate_violet_proof.py`

### 3. Macro-Galactic Dynamics & Cosmic Topology
* **`src/macro_dynamics.py`** | Interfaces directly with SPARC database parameter ranges, verifying flat galaxy rotation profiles without ad-hoc tracking parameters.
  * *Verification Runner:* `scripts/generate_macro_curves.py`
* **`notebooks/tully_fisher_derivation.ipynb`** | An interactive Jupyter notebook detailing the formal calculus integrating the OCM Hamiltonian into the exact $v^4 \propto M$ Tully-Fisher coefficient.
* **`src/tethering.py`** & **`src/lss_tethering.py`** | Simulates phase-locked cosmic dispersion and resolves the local satellite alignment paradox across cluster halos.
  * *Verification Runners:* `scripts/generate_tethering_plots.py`, `scripts/generate_lss_alignment.py`
* **`src/global_shear_parity.py`** & **`src/winding_resolution.py`** | Evaluates large-scale cosmic chirality and models viscous metric pitch angle preservation to solve spiral winding paradoxes.
  * *Verification Runners:* `scripts/generate_parity_plots.py`, `scripts/generate_winding_plots.py`

### 4. Sub-Critical, Failure, & Super-Critical Evolution
* **`src/sub_critical_dynamics.py`** | Tracks stellar-mass pulsar friction and recurrent nova metric shrug limits.
  * *Verification Runner:* `scripts/generate_sub_critical_plots.py`
* **`src/failure_modes.py`** | Probes magnetar core torsional failures and supernova metric bounce rebounds.
  * *Verification Runner:* `scripts/generate_failure_plots.py`
* **`src/super_critical_ignitions.py`** | Maps out kilonova splicing properties and tight polar GRB relativistic jet collimation vectors.
  * *Verification Runner:* `scripts/generate_super_critical_plots.py`

---

## 📈 Local Environment Verification

To install dependencies and re-render the entire suite of 14 verification figures locally, execute the following commands in your terminal:

```bash
# Clone the repository
git clone [https://github.com/your-username/ocm-core-framework.git](https://github.com/your-username/ocm-core-framework.git)
cd ocm-core-framework

# Install requirements
pip install -r requirements.txt

# Run a validation script (e.g., QPO 3:2 and Ghost Pulse validation)
python scripts/generate_qpo_spectra.py
