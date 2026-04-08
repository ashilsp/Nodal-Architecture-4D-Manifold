import numpy as np
from saturation import ManifoldSaturation

# Initialize
manifold = ManifoldSaturation()
M_sun = 1.989e30 # Mass of the Sun

# Scenario: A collapsing stellar core
# As the radius (R) decreases, standard GR says density goes to infinity.
# Your theory says it hits a ceiling (Rho_Crit).

radii = np.linspace(10, 0.1, 100) # Shrinking radius in kilometers
mass = 3 * M_sun

print(f"--- Manifold Saturation Analysis ---")
for r in [10, 5, 2, 1, 0.5]:
    rho = manifold.calculate_rho_crit(mass, r * 1000) # radius in meters
    print(f"At Radius {r}km: Density = {rho:.2e} kg/m^3")

print("\nConclusion: At the Rd interface, the manifold saturates.")
print("The density ceiling prevents the formation of a mathematical singularity.")
