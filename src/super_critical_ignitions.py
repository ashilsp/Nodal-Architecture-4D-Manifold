import numpy as np

def calculate_ignition_exhaust(S_M, angular_momentum_J=0.0):
    """
    Models the morphological state profiles of super-critical manifold ignitions.
    Calculates the distribution of radiated energy between isotropic exhaust 
    (Violet Shift) and collimated polar jet streams (Gamma-Ray Bursts).
    """
    if S_M <= 1.0:
        raise ValueError("This engine explicitly evaluates super-critical states where S_M > 1.0")
        
    # Latent heat of phase transition released during 3D-to-4D shift
    total_latent_energy = 10.0 * (S_M - 1.0)
    
    # Collimation efficiency is driven by the coupling of hyper-criticality and spin
    # Extreme angular momentum (J) restricts spherical discharge, forcing a polar funnel
    if S_M > 2.0 and angular_momentum_J > 5.0:
        collimation_factor = 1.0 - np.exp(-0.4 * angular_momentum_J)
        jet_energy = total_latent_energy * collimation_factor
        isotropic_violet_energy = total_latent_energy * (1.0 - collimation_factor)
        state_mode = "Hypernova / GRB Jet"
    else:
        jet_energy = 0.0
        isotropic_violet_energy = total_latent_energy
        state_mode = "Steady-State OCM Node"
        
    return state_mode, isotropic_violet_energy, jet_energy

def simulate_kilonova_splicing(time_steps):
    """
    Simulates the localized 'Splicing Spike' in metric tension when two 
    independent sub-critical gravity wells collide and force their 4D fabrics to unify.
    """
    # Models the dual-well phase collision peaking at the midpoint of the timeline
    midpoint = len(time_steps) // 2
    
    # Baseline sub-critical tension profiles climbing toward merger
    climb = np.linspace(0.4, 0.95, midpoint)
    
    # The instantaneous splicing spike at the exact collision point
    spike_amplitude = 3.5
    spike = np.array([spike_amplitude])
    
    # Post-merger stabilization dropping down into the steady-state node equilibrium
    stabilization = np.exp(-0.05 * np.arange(len(time_steps) - midpoint - 1)) + 1.1
    
    tension_profile = np.concatenate([climb, spike, stabilization])
    return tension_profile
