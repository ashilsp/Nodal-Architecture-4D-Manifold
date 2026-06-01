import numpy as np
import matplotlib.pyplot as plt
from src.super_critical_ignitions import calculate_ignition_exhaust, simulate_kilonova_splicing

# 1. Sweep Angular Momentum for a Hyper-Critical Core (S_M = 3.5)
spin_sweep = np.linspace(0, 10, 100)
isotropic_energies = []
jet_energies = []

for j in spin_sweep:
    _, iso, jet = calculate_ignition_exhaust(S_M=3.5, angular_momentum_J=j)
    isotropic_energies.append(iso)
    jet_energies.append(jet)

# 2. Simulate Kilonova Fabric Splicing Tension Timeline
timeline = np.linspace(0, 100, 200)
splicing_tension = simulate_kilonova_splicing(timeline)

# Build publication-grade side-by-side verification subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left Subplot: Polar Jet Collimation Analysis
ax1.plot(spin_sweep, isotropic_energies, color='darkviolet', linewidth=2, label='Isotropic Violet Exhaust')
ax1.plot(spin_sweep, jet_energies, color='darkorange', linestyle='--', linewidth=2.5, label='Collimated Polar GRB Jet')
ax1.axvline(5.0, color='red', linestyle=':', alpha=0.6, label='Centrifugal Funneling Threshold')
ax1.set_xlabel('Angular Momentum (Spin Parameter $J$)')
ax1.set_ylabel('Radiated Energy Release Intensity')
ax1.set_title('a) Jet Collimation as a Function of Centrifugal Strain ($S_M \\gg 1$)')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='center left')

# Right Subplot: Kilonova Splicing Timeline
ax2.plot(timeline, splicing_tension, color='crimson', linewidth=2, label='Local Manifold Tension ($S_M$)')
ax2.axhline(1.0, color='black', linestyle='-.', alpha=0.4, label='Critical Saturation Bound')
ax2.annotate('Instantaneous Splicing Spike\n(Baryonic Scrap Ejection)', xy=(50, 3.4), xytext=(65, 2.5),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6), fontsize=9)
ax2.set_xlabel('Merger Evolution Timeline ($t$)')
ax2.set_ylabel('Metric Tension Metric')
ax2.set_title('b) Kilonova Evolution: Dual Potential Well Fabric Fusion')
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('super_critical_ignitions_verification.png', dpi=300)
print("Success: 'super_critical_ignitions_verification.png' successfully compiled and saved.")
