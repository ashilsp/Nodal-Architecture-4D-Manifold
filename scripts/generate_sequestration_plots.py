import numpy as np
import matplotlib.pyplot as plt

# 1. Model the Dimensional Entropy Transition Phase Shift (S_3D -> S_2D + Delta_E)
radii = np.linspace(1.0, 5.0, 300)
R_d = 1.8

# As matter drops toward R_d, 3D chaotic degrees of freedom flatten out
S_3D = 5.0 * (1.0 - np.exp(-1.5 * (radii - R_d)))
S_3D[radii <= R_d] = 0.0  # Completely frozen/transitioned inside the shell

# 2D laminar entropy peaks right at the boundary wall layer
S_2D_laminar = np.exp(-8.0 * (radii - R_d)**2) * 1.5

# 2. Compute the 4D Mass-Energy Flux Integral Leakage Profile
# Phi_mass =oint (eta_M * grad_Psi_4D) dA. Represents systemic thermal noise floor.
manifold_viscosity_eta = 0.65
grad_psi_4D = np.exp(-0.5 * (radii - R_d)) / (radii ** 2)
phi_mass_flux = 4.0 * np.pi * (radii ** 2) * manifold_viscosity_eta * grad_psi_4D
phi_mass_flux[radii < R_d] = 0.8  # High-vacuum constant core tension flux value

# Build the publication layout figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left Panel: Dimensional Filtering Profile
ax1.plot(radii, S_3D, color='crimson', linewidth=2, label='Chaotic 3D Entropy ($S_{3D}$)')
ax1.plot(radii, S_2D_laminar, color='teal', linewidth=2.5, linestyle='--', label='Ordered 2D Laminar Entropy ($S_{2D}$)')
ax1.axvline(R_d, color='purple', linestyle=':', label='Disruption Boundary ($R_d$)')
ax1.set_xlabel('Radial Coordinate ($r$)')
ax1.set_ylabel('Entropy Degrees of Freedom')
ax1.set_title('a) Dimensional Compression Phase Transition')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='center right')

# Right Panel: 4D Conduit Mass-Energy Flux
ax2.plot(radii, phi_mass_flux, color='darkblue', linewidth=2, label=r'Mass Flux $\Phi_{mass}$ Conduit Flow')
ax2.fill_between(radii, 0, phi_mass_flux, where=(radii <= R_d), color='blue', alpha=0.08, label='High-Vacuum 4D Sink')
ax2.axvline(R_d, color='purple', linestyle=':', label='Boundary ($R_d$)')
ax2.set_xlabel('Radial Coordinate ($r$)')
ax2.set_ylabel('Mass-Energy Flux Intensity')
ax2.set_title('b) 4D Conduit Pressure Mitigation & Leakage')
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('entropy_sequestration_proof.png', dpi=300)
print("Success: 'entropy_sequestration_proof.png' compiled successfully.")
