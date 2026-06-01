import numpy as np

def compute_ocm_emission_spectrum(mass_scale, num_points=500):
    """
    Calculates the fundamental exhaust wavelength and energy gap profile 
    as a function of structural nodal mass scale.
    Implements the Mass-Frequency scale and Doppler geometry equations.
    """
    c = 299792458.0      # Speed of light (m/s)
    h_ev = 4.135667696e-15 # Planck's constant in eV*s
    
    # Baseline non-singular nucleon energy gap (~140 MeV for a standard proton-to-laminar transition)
    delta_E_base = 140.0e6 
    
    # Manifold damping factor Phi mimics spatial scaling and Doppler geometry adjustments.
    # As mass scales up, severe topological hardening drives the fundamental frequency higher.
    if mass_scale <= 50.0:
        # Stellar-mass regime: Pinning exhaust to Near/Far UV bands
        phi_manifold = 2.5e-8 / (1.0 + 0.01 * mass_scale)
    elif mass_scale <= 10e5:
        # Intermediate-mass regime: Soft X-Ray scaling
        phi_manifold = 5.0e-7 * (mass_scale**0.1)
    else:
        # Supermassive to Hypermassive core regimes: Hard X-Ray to Gamma-Ray scaling
        phi_manifold = 1.2e-5 * (mass_scale**0.25)
        
    # Calculate fundamental vibration frequency (nu)
    nu_fundamental = (delta_E_base / h_ev) * phi_manifold
    
    # Derive absolute exhaust wavelength lambda = c / nu
    lambda_exhaust_meters = c / nu_fundamental
    lambda_nm = lambda_exhaust_meters * 1e9
    
    # Generate an energy spectrum array centered around the fundamental peak (in eV)
    e_center = h_ev * nu_fundamental
    energy_axis = np.linspace(e_center * 0.1, e_center * 3.0, num_points)
    
    # Lorentzian line profile representing the stable background hum output
    width = e_center * 0.2
    flux_profile = (width**2) / ((energy_axis - e_center)**2 + width**2)
    
    return e_center, lambda_nm, energy_axis, flux_profile
