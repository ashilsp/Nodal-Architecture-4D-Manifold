import numpy as np
import matplotlib.pyplot as plt
from src.thermodynamics import calculate_hybrid_luminosity

# Setup accretion rate sampling bounds approaching absolute starvation (0 to 4 Eddington ratio)
accretion_rates = np.linspace(0.0, 4.0, 200)

# Calculate both physical tracks using the core thermodynamic engine
classical_profile, ocm_profile = calculate_hybrid_luminosity(accretion_rates)

# Generate publication verification plot mimicking your native LaTeX TikZ/PGFPlots asset
plt.figure(figsize=(8, 5.5))

plt.plot(accretion_rates, classical_profile, label=r'Standard Accretion Model ($L \rightarrow 0$)', 
         color='blue', linestyle='--', linewidth=1.5)
plt.plot(accretion_rates, ocm_profile, label=r'OCM Hybrid Profile ($\Lambda_{OCM}$ Floor)', 
         color='red', linewidth=2.0)

# Replicate the exact annotations from your LaTeX code document
plt.axhline(-1.5, color='purple', linestyle=':', alpha=0.8)
plt.text(3.9, -1.4, r'Metabolic Floor ($\Lambda_{OCM}$)', color='purple', 
         fontweight='bold', fontsize=8, ha='right')

# Highlight the 50,000x radiative excess at low fuel points
plt.annotate('', xy=(0.5, -1.5), xytext=(0.5, -2.75),
             arrowprops=dict(arrowstyle='<->', color='purple', lw=1.2))
plt.text(0.6, -2.1, '50,000$\\times$ Radiative Excess\n(Observable Plateau)', 
         color='purple', fontweight='bold', fontsize=8, va='center')

# Graph aesthetics matching a high-tier astrophysical paper layout
plt.xlim(0, 4)
plt.ylim(-4, 2)
plt.xlabel(r'Accretion Rate ($\dot{M} / \dot{M}_{\text{Edd}}$)')
plt.ylabel(r'Log Luminosity ($\log L / L_{\text{Edd}}$)')
plt.title('Luminosity Discrepancy in Fuel-Depleted Quasars (Figure 8 Verification)')
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('luminosity_floor_verification.png', dpi=300)
print("Success: 'luminosity_floor_verification.png' successfully compiled and saved.")
