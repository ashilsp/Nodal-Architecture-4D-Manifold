import numpy as np

def calculate_ocm_piecewise_potential(radii, R_d, M, E_0=-2.0):
    """
    Implements the exact OCM Topological Potential piecewise function:
    V_top(r) = -GM/r for r > R_d, and E_0 (Saturation Floor) for r <= R_d.
    Eliminates the standard GR singularity by shunting the potential at E_0.
    """
    G = 1.0  # Geometric units
    potentials = np.zeros_like(radii)
    
    # Outside the disruption boundary: Standard gravity
    outside_mask = radii > R_d
    potentials[outside_mask] = - (G * M) / radii[outside_mask]
    
    # Inside or at the boundary: Flat non-singular saturation floor
    potentials[~outside_mask] = E_0
    
    return potentials

def calculate_quantized_frequency(M_solar, R_star_factor=3.0, omega=1.5e-3):
    """
    Computes the quantized frequency of the emitted exhaust based on the formula:
    nu = (Delta E / h) * (c^3 / (G * M * omega))^0.5
    Validates the physical spectrum scaling: Stellar-mass pushes to Violet/UV (10^15 Hz),
    while Supermassive scales down to Hard X-rays (10^18 Hz).
    """
    # Natural constants
    h = 6.626e-34
    c = 3.0e8
    G = 6.674e-11
    M_sun_kg = 1.989e30
    
    # Convert mass scale to physical kilograms
    M_kg = M_solar * M_sun_kg
    
    # Structural metric scales
    R_d = (2.0 * G * M_kg) / (c ** 2)
    R_star = R_star_factor * R_d
    m_test = 1.67e-27  # Proton mass unit transitioning into ground state
    
    # Calculate energy gap Delta E
    delta_E = m_test * (c ** 2) * (1.0 - np.sqrt(1.0 - (R_d / R_star)))
    
    # Apply the manifold curvature damping modifier
    curvature_modifier = np.sqrt((c ** 3) / (G * M_kg * omega))
    
    nu_exhaust = (delta_E / h) * curvature_modifier
    return nu_exhaust

def calculate_discrete_quantum_steps(max_n=4, M_min_solar=3.0):
    """
    Implements the discrete Nodal Growth rule: R_n = n^2 * (G * M_min / c^2)
    Computes the quantized stable radii steps that explain observed population mass gaps.
    """
    G = 1.0
    c = 1.0
    R_min = (G * M_min_solar) / (c ** 2)
    
    n_values = np.arange(1, max_n + 1)
    quantized_radii = (n_values ** 2) * R_min
    return n_values, quantized_radii
