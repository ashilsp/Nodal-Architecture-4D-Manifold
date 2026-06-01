import numpy as np
import matplotlib.pyplot as plt
from src.macro_dynamics import calculate_velocity_curve

# Setup radial profiles out to 12 kpc
radii = np.linspace(100, 12000, 300)

# -------------------------------------------------------------
# CASE 1: Standard Active Spiral Galaxy (High-Capacity Node)
# -------------------------------------------------------------
M_spiral = 5e10
v_spiral_keplerian = calculate_velocity_curve(radii, M_spiral, eta_M=0.0, omega_core=0.0)
v_spiral_ocm = calculate_velocity_curve(radii, M_spiral, eta_M=4.5e-6, omega_core=2.1e-3)

# -------------------------------------------------------------
# CASE 2: Anomalous Galaxy NGC 1052-DF2 (Dormant Node Core)
# -------------------------------------------------------------
M_df2 = 2e8
v_df2_keplerian = calculate_velocity_curve(radii, M_df2, eta_M=0.0, omega_core=0.0, is_df2=True)
# DF2 features a dormant central node -> negligible kappa-flux -> zero viscosity stiffening
v_df2_ocm = calculate_velocity_curve(radii, M_df2, eta_M=1.0e-12, omega_core=0.0, is_df2=True)

# Generate publication layout panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Panel 1: High-Capacity Spiral Rotation Profile
ax1.plot(radii / 1000, v_spiral_keplerian, label='Keplerian (Baryonic Only Decay)', color='blue', linestyle='--')
ax1.plot(radii / 1000, v_spiral_ocm, label=r'OCM Viscosity ($\eta_M$ Saturation)', color='red', linewidth=2)
ax1.set_xlabel('Distance from Center $r$ (kpc)')
ax1.set_ylabel('Rotation Velocity $v$ (km/s)')
ax1.set_title('a) High-Mass Active Spiral System')
ax1.set_ylim(0, 250)
ax1.legend(loc='lower right')
ax1.grid(True, linestyle=':', alpha=0.5)

# Panel 2: Dormant Node Profile (NGC 1052-DF2 Simulation)
ax2.plot(radii / 1000, v_df2_keplerian, label='Keplerian Baseline', color='blue', linestyle='--')
ax2.plot(radii / 1000, v_df2_ocm, label='OCM Dormant Mode Profile', color='darkgreen', linewidth=2, linestyle=':')
ax2.set_xlabel('Distance from Center $r$ (kpc)')
ax2.set_ylabel('Rotation Velocity $v$ (km/s)')
ax2.set_title('b) Missing "Dark Matter" Exception: NGC 1052-DF2')
ax2.set_ylim(0, 30)
ax2.legend(loc='lower right')
ax2.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('macro_dynamics_verification.png', dpi=300)
print("Success: 'macro_dynamics_verification.png' successfully compiled and saved.")
