import numpy as np
import matplotlib.pyplot as plt
from src.manifold_viscosity import calculate_rotation_profile

# Define galactic testing parameters
radii = np.linspace(0, 15000, 300) # Radius out to 15 kpc
mass_core = 1e11                  # Solar masses in central core area
rho_baryon_base = 0.5             # Baseline mass distribution constant

# Scenario 1: Standard Newtonian profile (No manifold viscosity intervention)
eta_M_zero = 0.0
v_newtonian = calculate_rotation_profile(radii, mass_core, eta_M_zero, rho_baryon_base)

# Scenario 2: OCM Framework profile (With structural manifold viscosity)
eta_M_active = 1.2e-4
v_ocm = calculate_rotation_profile(radii, mass_core, eta_M_active, rho_baryon_base)

# Generate publication verification plot
plt.figure(figsize=(8, 5))
plt.plot(radii / 1000, v_newtonian, label='Standard Newtonian (Shear Decay Curve)', color='red', linestyle='--')
plt.plot(radii / 1000, v_ocm, label='OCM Manifold Viscosity Model (Flat Constant Profile)', color='blue', linewidth=2)
plt.xlabel('Galactic Radius $r$ (kpc)')
plt.ylabel('Orbital Velocity $v(r)$ (km/s)')
plt.title('Galactic Profile Verification: Section 6 Framework Execution')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig('rotation_curve_verification.png', dpi=300)
print("Success: 'rotation_curve_verification.png' successfully compiled and saved.")
