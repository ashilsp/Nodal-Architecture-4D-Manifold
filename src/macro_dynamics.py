import numpy as np

def calculate_velocity_curve(radii, M_baryon, eta_M, omega_core, is_df2=False):
    """
    Computes galactic rotation velocities using the OCM Viscous Tension Equation:
    v(r) = sqrt( (G * M(r) / r) + (eta_M * omega * r^2 / m) )
    
    If eta_M is zero (or the node is dormant like NGC 1052-DF2), it naturally 
    decays back to a classical baryonic Keplerian curve.
    """
    G = 4.30091e-3  # pc * (km/s)^2 / M_sun
    velocities = []
    
    # Simple bulge/disk mass distribution estimation inside radius r
    # NGC 1052-DF2 is much more diffuse than a standard compact spiral
    r_scale = 3000.0 if not is_df2 else 5000.0
    
    for r in radii:
        if r == 0:
            velocities.append(0)
            continue
            
        # Enclosed baryonic mass at radius r
        M_r = M_baryon * (1.0 - np.exp(-r / r_scale))
        
        # Newtonian Component
        v_grav_sq = (G * M_r) / r
        
        # OCM Manifold Coupling Viscous Tension Component
        # Derived from: (eta_M * Omega * r^2) / m
        v_viscous_sq = (eta_M * omega_core * (r**2)) / (1.0 + (r / r_scale))
        
        # Combine parameters to find total velocity
        v_total = np.sqrt(v_grav_sq + v_viscous_sq)
        velocities.append(v_total)
        
    return np.array(velocities)
