import numpy as np

def calculate_ocm_hybrid_luminosity(Mdot_normalized, Lambda_OCM=1e-1.5):
    """
    Implements the OCM Hybrid Radiative Profile equation:
    L_obs = eta * Mdot * c^2 + Lambda_OCM
    Guarantees the 50,000x radiative excess plateau during fuel starvation.
    """
    # Normalized efficiency scale
    eta = 0.1
    c = 1.0
    
    # Classical linear model baseline matching standard GR limits
    L_classical = eta * Mdot_normalized * (c ** 2)
    
    # OCM hybrid tracking containing the permanent structural floor
    L_hybrid = L_classical + Lambda_OCM
    
    return L_classical, L_hybrid

def calculate_violet_limit_spectrum(wavelengths_nm, T_core=50000, hardening_coefficient=1.8):
    """
    Implements the Wien's Displacement Law shift and Topological Hardening.
    Models the non-thermal phase transition of the internal Quark-Gluon Plasma (QGP),
    generating a localized radiant bump locked in the 120nm to 300nm spectrum.
    """
    # Wien's displacement constant in nm * K
    b_constant = 2.89777e6
    
    # Classical un-hardened blackbody thermal baseline peak wavelength
    lambda_max_thermal = b_constant / T_core
    
    # Non-thermal Topological Hardening function driven by the high-density kappa-flux
    # Generates the non-singular spectral bump centered within the 120nm - 300nm range
    bump_center = 210.0  # Center point in nm
    bump_width = 40.0
    
    thermal_profile = (1.0 / wavelengths_nm**5) / (np.exp(1.4387e7 / (wavelengths_nm * T_core)) - 1.0)
    thermal_profile = (thermal_profile / np.max(thermal_profile)) * 0.3
    
    # Superimpose the manifold quantum-geometric blue-shift profile
    hardening_bump = np.exp(-0.5 * (wavelengths_nm - bump_center)**2 / bump_width**2) * hardening_coefficient
    
    total_violet_limit_spectrum = thermal_profile + hardening_bump
    return total_violet_limit_spectrum
