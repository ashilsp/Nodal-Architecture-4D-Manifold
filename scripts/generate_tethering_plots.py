import numpy as np
import matplotlib.pyplot as plt
from src.tethering import simulate_cluster_dispersion

# Set up temporal tracking arrays (e.g., across hundreds of millions of years)
times = np.linspace(0, 500, 250)

# Scenario A: Classical cluster dispersion model (No underlying manifold seam structural anchor)
sigma_classical = simulate_cluster_dispersion(times, initial_dispersion=4.0, eta_M=0.0)

# Scenario B: OCM Coherent "Nodal Family" profile (Pleiades/Orion type structural lock)
sigma_ocm = simulate_cluster_dispersion(times, initial_dispersion=4.0, eta_M=0.15, a0_tension=1.4)

# Generate publication figure layout
plt.figure(figsize=(8.5, 5))

plt.plot(times, sigma_classical, label='Standard Physics: Ballistic Dispersal (Chaotic Decay)', 
         color='blue', linestyle='--', linewidth=1.5)
plt.plot(times, sigma_ocm, label=r'OCM Phase-Lock: Topological Tethering ($\eta_M$ Bound)', 
         color='purple', linewidth=2.5)

# Plot decoration parameters mimicking high-tier structural kinematics metrics
plt.xlabel('Evolutionary Timescale $t$ (Myr)')
plt.ylabel(r'Velocity Dispersion $\sigma_v$ (km/s)')
plt.title('Velocity Dispersion Stability in Co-Moving Clusters (Figure 10 Verification)')
plt.ylim(0, 10)
plt.xlim(0, 500)
plt.legend(loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('topological_tethering_verification.png', dpi=300)
print("Success: 'topological_tethering_verification.png' successfully compiled and saved.")
