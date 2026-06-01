import numpy as np
import matplotlib.pyplot as plt
from src.sub_critical_dynamics import simulate_pulsar_friction, simulate_nova_shrugging

# Setup timeline arrays for metrics sampling
time_pulsar = np.linspace(0, 0.1, 500)
time_nova = np.linspace(0, 1000, 1000)

# 1. Simulate Pulsar Topological Friction Profile at S_M = 0.92
pulsar_b_field = simulate_pulsar_friction(time_pulsar, S_M=0.92, spin_frequency=40.0)

# 2. Simulate Nova Recurrent Surface Shrugging (Constant binary companion mass feeding)
mass_stream = np.ones(1000) * 4.5e-7 
nova_mass_history, nova_eruptions = simulate_nova_shrugging(mass_stream, core_S_M=0.3)

# Build a dual-panel validation figure matching the manuscript layout specifications
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.5))

# Upper Panel: Pulsar Oscillations (Topological Friction)
ax1.plot(time_pulsar * 1000, pulsar_b_field, color='purple', linewidth=1.5, label='Beamed Magnetar Friction Intensity ($B$)')
ax1.set_xlabel('Time Coordinate (ms)')
ax1.set_ylabel('Friction Field Amplitude')
ax1.set_title('a) Pulsar Throat Bottleneck Mechanical Oscillations ($S_M \\to 1$)')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right')

# Lower Panel: Recurrent Nova Sawtooth Profile (Surface Shrugging)
ax2.plot(time_nova, nova_mass_history * 1e5, color='darkorange', linewidth=2, label='Accreted Envelope Envelope Mass')
# Highlight eruption trigger points where the manifold spring snaps back
eruption_indices = np.where(nova_eruptions == 1)[0]
ax2.vlines(eruption_indices, ymin=0, ymax=15, colors='red', linestrees='--', alpha=0.7, label='Manifold Surface Shrug (Nova)')

ax2.set_xlabel('Binary Accretion Timeline (Years)')
ax2.set_ylabel(r'Envelope Mass Accumulation ($10^{-5} M_\odot$)')
ax2.set_title('b) Recurrent Nova Boundary Clearance Cycles ($S_M < 1$ Core Stability)')
ax2.set_ylim(0, 15)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('sub_critical_states_verification.png', dpi=300)
print("Success: 'sub_critical_states_verification.png' successfully compiled and saved.")
