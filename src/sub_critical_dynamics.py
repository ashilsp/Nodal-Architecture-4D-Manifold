import numpy as np

def simulate_pulsar_friction(time_steps, S_M, spin_frequency=50.0):
    """
    Simulates the energy emission profile of a pulsar approaching the critical threshold (S_M -> 1).
    Models 'Topological Friction' where the core grinds against the 4D manifold envelope,
    converting rotational energy into periodic, beamed magnetic friction profiles (B).
    """
    # Friction amplitude increases non-linearly as S_M approaches 1
    friction_coefficient = 1.0 / (1.0 - S_M) if S_M < 1.0 else 100.0
    
    # Generate the periodic clock signals modulated by the manifold grinding resistance
    omega = 2.0 * np.pi * spin_frequency
    base_signal = np.sin(omega * time_steps)
    
    # Sharp beamed profiles caused by steep geometric throat constraints
    beamed_emissions = np.exp(5.0 * (base_signal - 1.0)) * friction_coefficient
    return beamed_emissions

def simulate_nova_shrugging(accreted_mass_stream, core_S_M=0.3):
    """
    Tracks the localized surface saturation metric of an accreting White Dwarf.
    When the surface layer hits the pseudo-critical threshold (S_M_surface -> 1),
    the compressed manifold acts as an elastic spring, 'shrugging' off the envelope.
    """
    surface_mass = 0.0
    shrug_trigger_threshold = 1.2e-4  # Solar masses needed to overload surface elasticity
    ejection_events = []
    mass_history = []
    
    for mass_increment in accreted_mass_stream:
        surface_mass += mass_increment
        current_surface_S_M = core_S_M + (surface_mass / shrug_trigger_threshold) * (1.0 - core_S_M)
        
        if current_surface_S_M >= 1.0:
            # Manifold violently rejects localized density perturbation: Surface Shrug Ejection
            ejection_events.append(1)  # Nova eruption triggered
            surface_mass = 0.0        # Reset envelope back to high-tension equilibrium
        else:
            ejection_events.append(0)
            
        mass_history.append(surface_mass)
        
    return np.array(mass_history), np.array(ejection_events)
