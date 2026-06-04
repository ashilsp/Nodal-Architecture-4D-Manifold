"""
Order-Creator Manifold (OCM) Framework
Module: Jeans Instability and Localized Stellar Clustering Mechanics
Path: src/jeans_instability.py
"""

import numpy as np
from scipy.spatial.distance import pdist

class OCMJeansSolver:
    def __init__(self, num_nodes=120, baseline_shear=1.2, manifold_viscosity=2.5):
        self.num_nodes = num_nodes
        self.shear_rate = baseline_shear
        self.eta_M = manifold_viscosity
        
        # Consistent seeding for structural replication across testing cycles
        np.random.seed(888)
        
        # Initialize dense isothermal molecular cloud radial configuration profile
        r_init = np.random.exponential(0.4, self.num_nodes)
        theta_init = np.random.uniform(0, 2 * np.pi, self.num_nodes)
        
        self.x_base = r_init * np.cos(theta_init)
        self.y_base = r_init * np.sin(theta_init)

    def compute_classical_decay(self, t=2.0):
        """Evaluates traditional Jeans mass fragmentation with unmitigated tidal shear."""
        # Standard linear differential velocity shearing along the tracking plane
        x_final = self.x_base + (self.y_base * self.shear_rate * t)
        # Thermal drift dispersion representing unconstrained phase-mixing
        y_final = self.y_base + np.random.normal(0, 0.15 * t, self.num_nodes)
        return x_final, y_final

    def compute_ocm_tethering(self, t=2.0):
        """Evaluates OCM equation of motion containing viscous dampening + lattice locking."""
        # Viscous dampening factor derived from the velocity gradient term: \eta_M \nabla^2 v
        damping = 1.0 / (1.0 + 4.0 * self.eta_M * t)
        
        # Core fluid masses lock onto the hidden manifold structural seams
        x_final = self.x_base + (self.y_base * self.shear_rate * t * damping)
        # F_\kappa grounding forces compress the coordinates toward local equilibrium
        y_final = self.y_base * (1.0 - 0.1 * t)
        return x_final, y_final

    def extract_spatial_metrics(self, x, y):
        """Calculates statistical invariants to track structural tightness over time."""
        coords = np.c_[x, y]
        distances = pdist(coords)
        return np.mean(distances), np.var(distances)
