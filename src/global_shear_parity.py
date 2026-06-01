import numpy as np

def run_parity_simulation(num_nodes, filament_tension=1.0):
    """
    Simulates Nodal ignition orientation probabilities based on the 
    energy efficiency delta: Delta E_prograde < Delta E_retrograde.
    """
    # Baseline ignition probabilities driven by the global shear field grain
    p_prograde_base = 2.0 / 3.0
    
    # Scale alignment bias upwards if the node resides within a high-tension filament
    if filament_tension > 1.0:
        p_prograde = min(0.85, p_prograde_base * (1.0 + 0.15 * (filament_tension - 1.0)))
    else:
        p_prograde = p_prograde_base
        
    # Run Monte Carlo selection across the target population
    samples = np.random.random(num_nodes)
    prograde_count = np.sum(samples < p_prograde)
    retrograde_count = num_nodes - prograde_count
    
    return prograde_count / num_nodes, retrograde_count / num_nodes
