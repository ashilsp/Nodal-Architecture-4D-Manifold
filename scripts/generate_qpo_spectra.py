import numpy as np
import matplotlib.pyplot as plt
from src.quantum_nodal_dynamics import calculate_ground_state_wavefunction, generate_qpo_power_spectrum

# Setup evaluation bounds
radii = np.linspace(0.1, 50.0, 500)
frequencies = np.linspace(10.0, 500.0, 1000)
R_d_boundary = 10.0          # Critical interface radius
f_fundamental = 100.0        # Baseline nodal vibration frequency (Hz)

# Calculate physical models
psi_0 = calculate_ground_state_wavefunction(radii, R_d_boundary)
psd = generate_qpo_power_spectrum(frequencies, f_fundamental)

# Construct dual-panel validation figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Panel A: Wavefunction Singular Mitigation Plot
ax1.plot(radii, psi_0, color='purple', linewidth=2, label=r'$\Psi_0$ Ground State')
ax1.axvline(R_d_boundary, color='black', linestyle=':', label=r'$R_d$ Interface Layer')
ax1.fill_between(radii, psi_0, alpha=0.15, color='purple')
ax1.set_xlabel('Manifold Coordinate Radius $r$')
ax1.set_ylabel('Probability Amplitude $|\Psi_0(r)|$')
ax1.set_title('a) Quantum Wall Transition (Non-Singularity Bounds)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel B: Power Spectral Density Plot (Twin Peaks & Ghost Pulse)
ax2.plot(frequencies, psd, color='darkblue', linewidth=1.5)
ax2.axvline(100.0, color='red', linestyle='--', alpha=0.7, label='1.0x Fundamental Peak')
ax2.axvline(150.0, color='orange', linestyle='--', alpha=0.7, label='1.5x Harmonic Peak (3:2 Ratio)')
ax2.axvline(300.0, color='gray', linestyle=':', alpha=0.7, label="Predicted 'Ghost Pulse'")
ax2.set_xlabel('Vibration Frequency $f$ (Hz)')
ax2.set_ylabel('Power Spectral Density (Arbitrary Units)')
ax2.set_title('b) Nodal Resonator Spectrum (QPO Simulation)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('quantum_qpo_verification.png', dpi=300)
print("Success: 'quantum_qpo_verification.png' successfully compiled and saved.")
