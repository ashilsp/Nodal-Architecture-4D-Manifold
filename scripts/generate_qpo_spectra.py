import numpy as np
import matplotlib.pyplot as plt
from src.quantum_nodal_dynamics import calculate_nodal_resonator_modes, simulate_qpo_spectrum_with_ghost_pulse

# Pick a reference microquasar stellar-mass node (e.g., 10 Solar Masses)
M_node = 10.0
f_toroidal, f_poloidal = calculate_nodal_resonator_modes(M_node)

# Generate active accreting state spectrum vs absolute zero accretion state
freqs, power_active = simulate_qpo_spectrum_with_ghost_pulse(accretion_rate_Mdot=1.0, 
                                                            base_f_toroidal=f_toroidal, 
                                                            base_f_poloidal=f_poloidal)

_, power_quiescent = simulate_qpo_spectrum_with_ghost_pulse(accretion_rate_Mdot=0.0, 
                                                           base_f_toroidal=f_toroidal, 
                                                           base_f_poloidal=f_poloidal)

# Initialize publication subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# Left Panel: Active High-Mass Accretion showing the clear Twin Peaks
ax1.plot(freqs, power_active, color='darkblue', linewidth=2, label='Accreting Flux Profile')
ax1.axvline(f_toroidal, color='red', linestyle='--', alpha=0.7, label=r'Toroidal Mode $f_T$')
ax1.axvline(f_poloidal, color='green', linestyle='--', alpha=0.7, label=r'Poloidal Mode $f_P$ (3:2)')
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Power Spectral Density')
ax1.set_title('a) Microquasar Twin-Peak kHz QPOs ($3:2$ Symmetry)')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend()

# Right Panel: Zero Accretion showing the persistent Ghost Pulse topological clock
ax2.plot(freqs, power_quiescent, color='purple', linewidth=2, label='Quiescent Ground State Hum')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Power Spectral Density')
ax2.set_title('b) The Ghost Pulse Prediction: Persistent Manifold Resonance')
ax2.set_ylim(0, 25)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.savefig('qpo_nodal_vibrations.png', dpi=300)
print(f"Success: 'qpo_nodal_vibrations.png' saved. Peaks at {f_toroidal:.1f} Hz and {f_poloidal:.1f} Hz.")
