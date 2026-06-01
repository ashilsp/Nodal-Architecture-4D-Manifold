import numpy as np

def compute_topological_potential(radii, R_d, M, C_kappa, n=2):
    """
    Computes the total OCM Topological Potential V_top(r) = V_grav(r) + V_kappa(r).
    As r approaches R_d from the outside, V_kappa creates an exponential 
    Quantum Wall that prevents singularity collapse.
    """
    # G and c set to 1 for normalized geometric units
    G = 1.0
    
    # Gravitational attractive potential
    V_grav = - (G * M) / radii
    
    # Initialize the exponential manifold repulsion term
    V_kappa = np.zeros_like(radii)
    
    # Apply the repulsion exclusively outside the disruption boundary
    valid_mask = radii > R_d
    V_kappa[valid_mask] = C_kappa / ((radii[valid_mask] - R_d) ** n)
    # Inside or at the boundary, clip to a massive finite value representing the wall
    V_kappa[~valid_mask] = 1e6
    
    V_total = V_grav + V_kappa
    return V_total, V_grav, V_kappa

def calculate_m87_eigenvalue_emission(M_solar=6.5e9):
    """
    Evaluates the M87* Eigenvalue Correlation.
    Calculates the energy transition Delta E as chaotic matter falls into the
    laminar ground state, outputs the corresponding spectrum range in keV.
    """
    # Matter reaching the photon sphere hits an un-stabilized kinetic threshold
    K_chaos_fraction = 0.15
    c = 3.0e8  # m/s
    electron_volt_joule = 1.602e-19
    
    # Average plasma mass unit energy transition scale
    mass_proton = 1.67e-27  # kg
    E_chaos = K_chaos_fraction * mass_proton * (c ** 2)
    E_0 = 0.0  # Normalized stable ground state level
    
    delta_E_joules = E_chaos - E_0
    delta_E_eV = delta_E_joules / electron_volt_joule
    delta_E_keV = delta_E_eV / 1000.0
    
    # Output the focused spectral bracket around the calculation target
    lower_bound_keV = delta_E_keV * 0.65
    upper_bound_keV = delta_E_keV * 6.5
    
    return lower_bound_keV, upper_bound_keV
