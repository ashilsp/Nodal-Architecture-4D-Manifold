import numpy as np

# Universal Constants from your paper
G = 6.67430e-11
A0 = 1.2e-10  # Manifold Saturation Constant from Supplement

class ManifoldSaturation:
    def __init__(self, epsilon_m=1.0):
        self.epsilon_m = epsilon_m

    def calculate_sm(self, density, curvature):
        """Equation 2: Sm = (D * Phi) / epsilon_M"""
        return (density * curvature) / self.epsilon_m

    def get_tully_fisher_velocity(self, mass):
        """Equation S9: v^4 = G * a0 * M"""
        return (G * A0 * mass)**(1/4)

    def calculate_rho_crit(self, mass, rd_radius):
        """Equation 3: rho_crit = 3M / (4 * pi * Rd^3)"""
        return (3 * mass) / (4 * np.pi * rd_radius**3)
