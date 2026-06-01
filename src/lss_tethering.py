import numpy as np

def simulate_satellite_planar_alignment(num_satellites, timesteps, gyro_strength=0.0):
    """
    Simulates the spatial collapse of satellite orbits from an initial 
    spherical distribution into a highly organized, thin disk.
    
    Models the Plane of Satellites Paradox via the Equatorial Manifold Fold vector.
    If gyro_strength is zero (Standard GR), the distribution stays spherically chaotic.
    """
    # Initialize random 3D position vectors on a unit sphere
    np.random.seed(42)
    theta = np.random.uniform(0, 2 * np.pi, num_satellites)
    phi = np.arccos(np.random.uniform(-1, 1, num_satellites))
    
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi) # Elevation tracking coordinate axis
    
    z_evolution = []
    
    for t in timesteps:
        if gyro_strength == 0.0:
            # Classical Gravity: Satellite positions maintain random spherical velocity parameters
            z_noise = z + np.random.normal(0, 0.01, num_satellites)
            z_evolution.append(np.std(z_noise))
        else:
            # OCM Gyroscopic Correction: Equatorial pressure forces dampening of out-of-plane elevation
            # Damping factor reduces z-axis variance over time proportional to the manifold fold tension
            damping_vector = np.exp(-gyro_strength * t)
            z_attenuated = z * damping_vector + np.random.normal(0, 0.005, num_satellites)
            z_evolution.append(np.std(z_attenuated))
            
    return np.array(z_evolution)
