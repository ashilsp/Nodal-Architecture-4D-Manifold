import numpy as np
import matplotlib.pyplot as plt
from src.lss_tethering import simulate_satellite_planar_alignment

# Define evolutionary tracking steps (e.g., across orbital scale steps)
intervals = np.linspace(0, 10, 150)

# Track Case A: Classical Stochastic Gravitational Capture (No plane locking)
variance_classical = simulate_satellite_planar_alignment(num_satellites=50, timesteps=intervals, gyro_strength=0.0)

# Track Case B: OCM Equatorial Fold Lock (Topological Gyroscope active)
variance_ocm = simulate_satellite_planar_alignment(num_satellites=50, timesteps=intervals, gyro_strength=0.35)

# Generate publication layout
plt.figure(figsize=(8.5, 5))

plt.plot(intervals, variance_classical, label=r'Standard $\Lambda$CDM: Isotropic Spherical Shell (Chaos)', 
         color='blue', linestyle='--', linewidth=1.5)
plt.plot(intervals, variance_ocm, label='OCM Network: Equatorial Manifold Fold (Thin Plane Lock)', 
         color='darkred', linewidth=2.5)

# Graph aesthetics matching cosmological metric layouts
plt.xlabel('System Evolution Scale $t$')
plt.ylabel('Out-of-Plane Thickness Variance ($\sigma_z$)')
plt.title('Resolution of the Plane of Satellites Paradox (Figure 11 Verification)')
plt.ylim(0.0, 0.8)
plt.xlim(0, 10)
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('plane_of_satellites_verification.png', dpi=300)
print("Success: 'plane_of_satellites_verification.png' successfully compiled and saved.")
