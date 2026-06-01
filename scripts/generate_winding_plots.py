import numpy as np
import matplotlib.pyplot as plt
from src.winding_resolution import simulate_spiral_arm_evolution

# Execute evolution sweeps across 3 full galactic core rotations
x_classical, y_classical = simulate_spiral_arm_evolution(num_stars=300, rotations=3.0, nu_M=0.0)
x_ocm, y_ocm = simulate_spiral_arm_evolution(num_stars=300, rotations=3.0, nu_M=0.45)

# Build publication-grade side-by-side verification subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

# Panel 1: Classical Differential Shear Destruction
ax1.plot(x_classical, y_classical, '.', color='crimson', markersize=3, label='Smeared Stellar Arm')
ax1.set_xlabel('Galactic X-Axis (kpc)')
ax1.set_ylabel('Galactic Y-Axis (kpc)')
ax1.set_title('a) Standard Newtonian Differential Shear (Winding Breakdown)')
ax1.set_xlim(-11, 11)
ax1.set_ylim(-11, 11)
ax1.grid(True, linestyle=':', alpha=0.4)
ax1.legend(loc='upper right')
ax1.set_aspect('equal')

# Panel 2: OCM Laminar Flux Stabilization
ax2.plot(x_ocm, y_ocm, '.', color='darkblue', markersize=4, label='OCM Laminar Flux Channel')
ax2.set_xlabel('Galactic X-Axis (kpc)')
ax2.set_ylabel('Galactic Y-Axis (kpc)')
ax2.set_title(r'b) OCM Framework Validation ($\nu_M \nabla^2 \mathbf{v}$ Locked Profile)')
ax2.set_xlim(-11, 11)
ax2.set_ylim(-11, 11)
ax2.grid(True, linestyle=':', alpha=0.4)
ax2.legend(loc='upper right')
ax2.set_aspect('equal')

plt.tight_layout()
plt.savefig('winding_problem_resolution.png', dpi=300)
print("Success: 'winding_problem_resolution.png' successfully compiled and saved.")
