import numpy as np
import matplotlib.pyplot as plt
from src.failure_modes import calculate_torsional_knotting

# Setup a sweep of the Manifold Saturation index approaching criticality
sm_sweep = np.linspace(0.5, 1.04, 200)
high_spin_J = 4.0

torsion_profiles = []
b_field_profiles = []

for sm in sm_sweep:
    tau, B = calculate_torsional_knotting(high_spin_J, sm)
    torsion_profiles.append(tau)
    b_field_profiles.append(B)

# Generate publication-grade figure layout
fig, ax1 = plt.subplots(figsize=(8.5, 5))

color = 'purple'
ax1.set_xlabel('Manifold Saturation Index ($S_M$)')
ax1.set_ylabel(r'Manifold Torsion ($\tau$)', color=color)
ax1.plot(sm_sweep, torsion_profiles, color=color, linewidth=2, label='Manifold Torsion Coordinate Twist')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle=':', alpha=0.5)

# Instantiating a second y-axis that shares the same x-axis for the B-field projection
ax2 = ax1.twinx()  
color = 'darkorange'
ax2.set_ylabel(r'Projected 3D Magnetic Flux ($B \propto \tau$)', color=color)
ax2.plot(sm_sweep, b_field_profiles, color=color, linestyle='--', linewidth=2, label='Electromagnetic Field Projection')
ax2.tick_params(axis='y', labelcolor=color)

# Highlight the Magnetar Torsional Crisis Zone (S_M approaching 1)
plt.axvspan(0.95, 1.01, color='red', alpha=0.1, label='Torsional Crisis Domain')

plt.title('Manifold Torsion and Magnetic Field Amplification (Figure 14 Verification)')
fig.tight_layout()
plt.savefig('failure_modes_verification.png', dpi=300)
print("Success: 'failure_modes_verification.png' successfully compiled and saved.")
