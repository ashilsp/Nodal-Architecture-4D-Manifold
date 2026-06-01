import numpy as np
import matplotlib.pyplot as plt
from src.global_shear_parity import run_parity_simulation

# Define population sizes
num_galaxies = 10000

# Calculate distributions across varying cosmic landscapes
void_prograde, void_retro = run_parity_simulation(num_galaxies, filament_tension=1.0)
filament_prograde, filament_retro = run_parity_simulation(num_galaxies, filament_tension=1.8)

print(f"Void Sample Distribution: Prograde={void_prograde:.4f}, Retrograde={void_retro:.4f}")
print(f"Filament Sample Distribution: Prograde={filament_prograde:.4f}, Retrograde={filament_retro:.4f}")

# Generate simple confirmation bar output
categories = ['Void Prograde', 'Void Retrograde', 'Filament Prograde', 'Filament Retrograde']
values = [void_prograde, void_retro, filament_prograde, filament_retro]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color=['gray', 'lightgray', 'blue', 'red'], alpha=0.8)
plt.ylabel('Statistical Population Ratio')
plt.title('Cosmic Parity Verification: Section 7 Energy Efficiency Alignment Model')
plt.ylim(0, 1.0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('cosmic_parity_verification.png', dpi=300)
print("Success: 'cosmic_parity_verification.png' successfully compiled and saved.")
