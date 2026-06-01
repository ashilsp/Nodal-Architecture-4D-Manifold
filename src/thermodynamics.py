import numpy as np

def calculate_hybrid_luminosity(accretion_rates, eta=0.1, lambda_ocm=10**(-1.5)):
    """
    Computes observed quasar luminosity comparing classical GR decay 
    against the OCM framework's internal 4D bridge leakage floor.
    
    Equation: L_obs = eta * M_dot * c^2 + Lambda_OCM
    """
    # Classical model tracking strictly mass-inflow rate
    # Modeled logarithmically to match standard astrophysical scaling tracking: 1.5*x - 3.5
    classical_luminosity = 1.5 * accretion_rates - 3.5
    
    # Convert back from log space to absolute values to perform the OCM addition
    absolute_classical = 10**(classical_luminosity)
    
    # OCM Hybrid integration (Classical dynamic flux + invariant geometric leakage floor)
    absolute_ocm = absolute_classical + lambda_ocm
    ocm_log_luminosity = np.log10(absolute_ocm)
    
    return classical_luminosity, ocm_log_luminosity
