import numpy as np

def classify_manifold_event(S_M, is_terminal_shrug=False):
    """
    Implements the OCM Classification of Rejection and Ignition Events (Table 4).
    Returns the event classification name, manifold action, and structural status.
    """
    if S_M < 1.0:
        if is_terminal_shrug:
            return "Type Ia SN", "Critical Shrug", "Complete 3D Disruption"
        else:
            return "Nova", "Surface Shrugging", "Periodic 3D Clearance"
    elif np.isclose(S_M, 1.0) or (S_M >= 1.0 and is_terminal_shrug):
        # High entropy or structural asymmetry blocks smooth puncture
        return "Type II SN", "Structural Rebound", "High-Entropy Nebula"
    else:
        # S_M > 1.0 with orderly geometric constraints
        return "OCM Node", "Laminar Puncture", "Stable 4D Bridge Interface"

def calculate_torsional_knotting(angular_momentum_J, S_M):
    """
    Models the Torsional Crisis regime (Magnetars). 
    Calculates the 3D projected magnetic flux field B as a direct 
    manifestation of manifold torsion (tau) when S_M approaches 1.0.
    """
    # Torsion scales non-linearly with asymmetric rotation near the puncture limit
    proximity_factor = 1.0 / (1.05 - np.clip(S_M, 0.0, 1.0))
    tau = angular_momentum_J * proximity_factor
    
    # B field is proportional to manifold torsion (B proportional to tau)
    B_field = 1.25 * tau
    return tau, B_field
