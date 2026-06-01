import numpy as np

def simulate_spiral_arm_evolution(num_stars=200, rotations=3.0, nu_M=0.0):
    """
    Simulates the geometric evolution of a galactic spiral arm over multiple rotations.
    Tracks structural winding by comparing Newtonian differential shear against 
    OCM Manifold Viscosity stabilization.
    
    If nu_M > 0, the viscous diffusion term counteracts the velocity gradient,
    preventing the arm from wrapping into a tightly smeared, unobservable mess.
    """
    # Initialize stars along a clean initial spiral arm trajectory
    radii = np.linspace(1.0, 10.0, num_stars)
    initial_phase = 0.5 * radii  # Initial trailing angle profile
    
    # Standard Newtonian velocity profile (v proportional to r^-0.5)
    v_keplerian = 5.0 / np.sqrt(radii)
    omega_keplerian = v_keplerian / radii
    
    # Calculate effective tracking time based on requested central rotations
    total_time = (2.0 * np.pi * rotations) / omega_keplerian[0]
    
    if nu_M == 0.0:
        # Case A: Classical GR - severe differential shear windup
        final_phase = initial_phase + (omega_keplerian * total_time)
    else:
        # Case B: OCM Viscous Coupling - regularizes orbital domains into an angular lock
        # The diffusion term (nu_M * del_squared_v) forces a uniform angular velocity profile
        omega_locked = omega_keplerian[0] * np.exp(-nu_M * radii) + (omega_keplerian[-1] * (1.0 - np.exp(-nu_M * radii)))
        # Blend based on viscosity strength to show smooth stabilization transition
        omega_effective = np. Lerp if hasattr(np, 'interp') else (omega_keplerian + nu_M * (omega_locked - omega_keplerian))
        # Clamp effective omega to protect physical coherence
        omega_effective = np.clip(omega_effective, omega_keplerian[-1], omega_keplerian[0])
        final_phase = initial_phase + (omega_effective * total_time)
        
    # Convert polar tracking back to Cartesian coordinates for direct plotting
    x = radii * np.cos(final_phase)
    y = radii * np.sin(final_phase)
    
    return x, y
