import numpy as np

def calculate_nodal_resonator_modes(M_solar, sigma_M=1.5, rho_manifold=1.0):
    """
    Implements the OCM Nodal Resonator Frequency framework.
    Calculates the fundamental frequency (v_pulse) and splits it into 
    coupled Poloidal (vertical) and Toroidal (torsional rotational) modes 
    enforced by the geometry of the Oloid-topology.
    """
    c = 3.0e8  # m/s
    G = 6.674e-11
    M_sun_kg = 1.989e30
    
    # Calculate physical disruption radius Rd for the node mass
    M_kg = M_solar * M_sun_kg
    R_d = (2.0 * G * M_kg) / (c ** 2)
    
    # Fundamental vibration frequency equation from the manuscript
    # v_pulse = (c / (2 * pi * R_d)) * sqrt(sigma_M / rho_manifold)
    v_fundamental = (c / (2.0 * np.pi * R_d)) * np.sqrt(sigma_M / rho_manifold)
    
    # The geometry of the Oloid-topology naturally enforces a 3:2 twin-peak resonance
    f_toroidal = v_fundamental * 1.0  # Base resonance component
    f_poloidal = v_fundamental * 1.5  # 3:2 paired coupled peak
    
    return f_toroidal, f_poloidal

def simulate_qpo_spectrum_with_ghost_pulse(accretion_rate_Mdot, base_f_toroidal, base_f_poloidal):
    """
    Simulates the QPO frequency power spectrum. 
    Implements the 'Ghost Pulse' prediction: even when accretion_rate -> 0,
    the structural manifold hum persists at its ground-state resonant modes.
    """
    frequencies = np.linspace(10, 2000, 1000)
    
    # Gas accretion dictates background chaotic noise amplitude
    gas_noise = (frequencies ** -1.2) * 50.0 * accretion_rate_Mdot
    
    # Manifold Ground-State Hum (The Ghost Pulse Core Amplitude)
    # This remains active as a baseline topological clock regardless of gas fuel
    manifold_hum_amplitude = 5.0 
    
    # Add the Toroidal peak
    peak_T = 15.0 * np.exp(-0.5 * (frequencies - base_f_toroidal)**2 / 25.0) * (accretion_rate_Mdot + 0.1)
    # Add the Poloidal peak (forming the 3:2 ratio)
    peak_P = 10.0 * np.exp(-0.5 * (frequencies - base_f_poloidal)**2 / 30.0) * (accretion_rate_Mdot + 0.1)
    
    # Build persistent ground state hum signal if accretion goes completely dead
    ghost_pulse_hum = (np.exp(-0.5 * (frequencies - base_f_toroidal)**2 / 5.0) + \
                       np.exp(-0.5 * (frequencies - base_f_poloidal)**2 / 5.0)) * manifold_hum_amplitude
    
    power_spectrum = gas_noise + peak_T + peak_P + ghost_pulse_hum
    return frequencies, power_spectrum
