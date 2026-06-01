import numpy as np

def simulate_cluster_dispersion(time_steps, initial_dispersion=5.0, eta_M=0.0, a0_tension=1.0):
    """
    Simulates the structural velocity dispersion (sigma_v) of a stellar cluster over time.
    Compares ballistic drift against OCM Topological Tethering (Aharonov-Bohm phase coupling).
    
    If eta_M > 0, the manifold impedance dampens chaotic 3D shear, locking the cluster members 
    into a coherent phase profile ("Beads-on-a-String").
    """
    dispersion_profile = []
    current_sigma = initial_dispersion
    
    for t in time_steps:
        if eta_M == 0:
            # Classical Regime: Unbound ballistic thermal drift leads to systematic dispersion increase
            current_sigma += 0.05 * np.sqrt(t) + np.random.normal(0, 0.02)
        else:
            # OCM Structural Regime: Wavefunction impedance prevents spatial unraveling
            # Damping factor scales as a function of manifold stiffness/viscosity
            damping = 1.0 / (1.0 + (eta_M * a0_tension * t**0.5))
            current_sigma = (initial_dispersion * damping) + np.random.normal(0, 0.01)
            
        # Ensure physical boundaries (dispersion cannot drop beneath absolute phase alignment zero)
        dispersion_profile.append(max(0.1, current_sigma))
        
    return np.array(dispersion_profile)
