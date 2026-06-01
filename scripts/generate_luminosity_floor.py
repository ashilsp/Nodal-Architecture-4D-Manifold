import numpy as np
import matplotlib.pyplot as plt
from src.thermodynamics import calculate_ocm_hybrid_luminosity, calculate_violet_limit_spectrum

# 1. Recreate the Luminosity Discrepancy Floor (Manuscript Figure 8 data)
mdot_sweep = np.linspace(0.0, 4.0, 200)
l_classical_list = []
l_hybrid_list = []

for m in mdot_sweep:
    l_class, l_hyb = calculate_ocm_hybrid_luminosity(m)
    l_classical_list.append(l_class)
    l_hybrid_list.append(l_hyb)

# 2. Sweep wavelengths for the QGP Topological Hardening Spectrum
wavelengths = np.linspace(50, 500, 300)
violet_limit_flux = calculate_violet_limit_spectrum(wavelengths)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left Panel: Exactly reproduce Manuscript Figure 8 layout
ax1.plot(mdot_sweep, np.log10(np.clip(l_classical_list, 1e-6, None)), 'b--', linewidth=1.5, label='Standard Accretion ($L \\to 0$)')
ax1.plot(mdot_sweep, np.log10(l_hybrid_list), 'r-', linewidth=2.5, label=r'OCM Hybrid Profile ($\Lambda_{OCM}$ Floor)')
ax1.axhline(-1.5, color='purple', linestyle=':', label='Metabolic Floor')
ax1.set_xlabel(r'Accretion Rate ($\dot{M} / \dot{M}_{Edd}$)')
ax1.set_ylabel(r'Log Luminosity ($\log L / L_{Edd}$)')
ax1.set_title('a) Luminosity Discrepancy in Fuel-Depleted Quasars')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='lower right')

# Right Panel: The Violet Limit Blackbody Decoupling Bump
ax2.plot(wavelengths, violet_limit_flux, color='darkviolet', linewidth=2.5, label='Internal QGP Boundary Emission')
ax2.axvspan(120, 300, color='magenta', alpha=0.12, label='Topological Hardening Domain')
ax2.set_xlabel('Wavelength $\\lambda$ (nm)')
ax2.set_ylabel('Normalized Radiant Flux Intensity')
ax2.set_title(r'b) The Internal "Violet Limit" Spectral Signature')
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('thermodynamic_metabolic_floor.png', dpi=300)
print("Success: 'thermodynamic_metabolic_floor.png' updated with the Violet Limit QGP spectrum.")
