import numpy as np
import matplotlib.pyplot as plt
from src.ocm_hamiltonian import calculate_ocm_piecewise_potential, calculate_quantized_frequency, calculate_discrete_quantum_steps

# 1. Generate Piecewise Potential Comparison Data
radii = np.linspace(0.1, 4.0, 500)
R_d, M = 1.0, 1.0
v_top = calculate_ocm_piecewise_potential(radii, R_d, M)
v_singularity = -1.0 / radii

# 2. Sample Mass-Scale Frequency Quantization Curves
mass_scales = np.logspace(1, 9, 100)  # Sweep from 10 to 10^9 solar masses
frequencies = [calculate_quantized_frequency(m) for m in mass_scales]

# 3. Compute Discrete Nodal Expansion Steps
n_steps, r_steps = calculate_discrete_quantum_steps(max_n=4)

# Construct a publication-grade multi-panel verification layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left Panel: Piecewise Saturation Floor Potential (Matching Figure 11 Geometry)
ax1.plot(radii, v_singularity, 'r--', alpha=0.6, label='GR Singularity ($V \\to -\\infty$)')
ax1.plot(radii, v_top, 'b-', linewidth=2.5, label='OCM Potential Floor ($V_{top}$)')
ax1.axvline(R_d, color='purple', linestyle=':', label='Boundary ($R_d$)')
ax1.fill_between(radii, -4, 1.5, where=(radii <= R_d), color='red', alpha=0.07, label='Shunted Zone')
ax1.set_xlabel('Radius ($r$)')
ax1.set_ylabel('Potential Energy $V(r)$')
ax1.set_title('a) Non-Singular OCM Piecewise Potential Well')
ax1.set_ylim(-3.5, 0.5)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='lower right')

# Right Panel: Mass-Scale Exhaust Frequency Scaling (Quantization Predictive Proof)
ax2.loglog(mass_scales, frequencies, color='darkorange', linewidth=2, label=r'$\nu_{exhaust}$ Quantization Curve')
# Highlight stellar vs supermassive observational targets
ax2.plot(10.0, calculate_quantized_frequency(10.0), 'ro', markersize=8, label='Stellar Node (~10^15 Hz UV)')
ax2.plot(6.5e9, calculate_quantized_frequency(6.5e9), 'bx', markersize=9, markeredgewidth=2, label='M87* Node (~10^18 Hz X-Ray)')
ax2.set_xlabel('Node Mass ($M_{\\odot}$)')
ax2.set_ylabel('Quantized Frequency $\\nu$ (Hz)')
ax2.set_title('b) Mass-Dependent Emission Spectral Shift')
ax2.grid(True, which="both", linestyle=':', alpha=0.4)
ax2.legend(loc='lower left')

plt.tight_layout()
plt.savefig('ocm_hamiltonian_foundations.png', dpi=300)
print("Success: 'ocm_hamiltonian_foundations.png' successfully compiled and saved.")
