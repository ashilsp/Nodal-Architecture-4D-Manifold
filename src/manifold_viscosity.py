import numpy as np

def calculate_rotation_profile(radii, mass_core, eta_M, rho_baryon_base):
    """
    Computes galactic orbital velocities by adding kinematic manifold viscosity 
    diffusion to standard gravitational potentials.
    """
    G = 4.30091e-3  # pc * (km/s)^2 / M_sun
    velocities = []
    
    for r in radii:
        if r == 0:
            velocities.append(0)
            continue
            
        # Standard Newtonian velocity component
        v_grav_sq = (G * mass_core) / r
        
        # Localized baryon density profile (falls off with radius)
        rho_r = rho_baryon_base * np.exp(-r / 3500.0) 
        
        # Kinematic viscosity calculation (nu_M = eta_M / rho)
        nu_M = eta_M / (rho_r + 1e-10)
        
        # Viscous space-stiffening coupling term smoothing the velocity gradient
        v_viscous_stabilisation = np.sqrt(nu_M * (v_grav_sq / r))
        
        # Total effective coupling velocity
        v_total = np.sqrt(v_grav_sq) + v_viscous_stabilisation
        velocities.append(v_total)
        
    return np.array(velocities)
