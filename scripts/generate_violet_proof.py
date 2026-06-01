import numpy as np
import matplotlib.pyplot as plt
from src.forensics import compute_ocm_emission_spectrum

# Setup testing configurations based on Table 2 mass benchmarks
targets = [
    {'name': 'Stellar-Mass Isolated (10 M_sun)', 'mass': 10.0, 'color': 'purple'},
    {'name': 'Intermediate Core (10^4 M_sun)', 'mass': 1e4, 'color': 'teal'},
    {'name': 'Supermassive Sgr A* (4x10^6 M_sun)', 'mass': 4e6, 'color': 'darkblue'},
    {'name': 'Hypermassive M87* (6x10^9 M_sun)', 'mass': 6e9, 'color': 'red'}
]

plt.figure(figsize=(10, 6))

for target in targets:
    e_peak, l_nm, energy_axis, flux = compute_ocm_emission_spectrum(target['mass'])
    
    # Format readable labels documenting mass-to-wavelength correlation parameters
    if l_nm >= 1.0:
        lbl = f"{target['name']} | $\lambda$ = {l_nm:.1f} nm"
    else:
        lbl = f"{target['name']} | $\lambda$ = {l_nm*1000:.1f} pm"
        
    plt.plot(energy_axis, flux, label=lbl, color=target['color'], linewidth=2)
    plt.fill_between(energy_axis, flux, alpha=0.08, color=target['color'])

# Configure publication-grade aesthetics matching standard spectroscopic plots
plt.xscale('log')
plt.xlabel('Exhaust Photon Energy $E$ (eV)')
plt.ylabel('Normalized Emission Intensity')
plt.title('OCM Color Rule Verification: Relativistic Mass-Frequency Scaling Suite')
plt.legend(loc='upper right', fontsize=9)
plt.grid(True, which="both", linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('violet_proof_scaling.png', dpi=300)
print("Success: 'violet_proof_scaling.png' successfully compiled and saved.")
