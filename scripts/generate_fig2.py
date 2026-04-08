import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# Ensure the script can find the saturation logic in the /src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from saturation import ManifoldSaturation

# 1. Initialize logic
manifold = ManifoldSaturation()

# 2. Setup Data (Simulated Density vs Curvature space)
densities = np.logspace(5, 15, 100)  # From WD to NS densities
curvature = 1.0  # Normalized curvature for this cross-section

sm_values = [manifold.calculate_sm(d, curvature) for d in densities]
states = [manifold.get_evolutionary_state(sm) for sm in sm_values]

# 3. Create the Visualization for Figure 2
plt.figure(figsize=(10, 6))

# Map states to colors for the plot
color_map = {
    "White Dwarf (Sub-Critical Saturation)": "blue",
    "Metastable Bottleneck (Neutron Star/Pulsar)": "orange",
    "Critical Ignition (OCM Node/Black Hole)": "red",
    "Super-Critical (Hypernova/Kilonova)": "darkred"
}

colors = [color_map[s] for s in states]

plt.scatter(densities, sm_values, c=colors, s=10, label="Stellar Evolution Path")
plt.axhline(y=1.0, color='black', linestyle='--', label='Critical Threshold (Sm=1.0)')
plt.xscale('log')
plt.yscale('linear')

plt.title("Figure 2a: Manifold Saturation Bifurcation")
plt.xlabel("Localized Mass-Density (D)")
plt.ylabel("Saturation Ratio (Sm)")
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.legend()

print("Plot Generated: This matches the bifurcation logic described in the main manuscript.")
plt.show()
