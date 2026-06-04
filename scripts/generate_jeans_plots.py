"""
Order-Creator Manifold (OCM) Framework
Script: Generate Jeans Instability Deconstruction Plots
Path: scripts/generate_jeans_plots.py
"""

import os
import sys
import matplotlib.pyplot as plt
import numpy as np

# Ensure root directories are accessible by Python's module compiler paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.jeans_instability import OCMJeansSolver

def main():
    print("Initializing OCM Jeans Instability Numerical Solver...")
    
    # Instantiate solver module using configured paper variables
    solver = OCMJeansSolver(num_nodes=120, baseline_shear=1.4, manifold_viscosity=2.5)
    
    # Calculate both physical states at final snapshot integration boundaries
    xn, yn = solver.compute_classical_decay(t=2.0)
    xo, yo = solver.compute_ocm_tethering(t=2.0)
    
    # Extract structural density statistics
    mean_sep_n, var_n = solver.extract_spatial_metrics(xn, yn)
    mean_sep_o, var_o = solver.extract_spatial_metrics(xo, yo)

    # Initialize a clean, dark profile layout matching your presentation figures
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), facecolor='#060709')
    fig.subplots_adjust(top=0.85, bottom=0.15, wspace=0.15)

    # Panel A Configuration: Newtonian Decay
    ax1.set_facecolor('#090a0f')
    ax1.scatter(solver.x_base, solver.y_base, color='gray', s=12, alpha=0.25, label='Initial Cloud Gas')
    ax1.scatter(xn, yn, color='#ff4444', s=20, alpha=0.85, edgecolors='#ffffff', linewidths=0.2, label='Sheared Cluster')
    ax1.set_xlim(-4, 4); ax1.set_ylim(-4, 4); ax1.set_aspect('equal'); ax1.axis('off')
    ax1.set_title("Classical Jeans Instability Collapse\n(Standard Galactic Shear Dispersal)", color='#ff5555', fontsize=11, weight='bold')
    ax1.legend(facecolor='#13141f', edgecolor='none', labelcolor='white', loc='lower right')
    
    # Left Telemetry Box
    ax1.text(-3.8, -3.8, f"Mean Separation : {mean_sep_n:.2f} pc\nSpatial Variance: {var_n:.2f}", 
             color='#ffaa66', fontname='monospace', fontsize=9, bbox=dict(boxstyle='round,pad=0.4', fc='#0d0e12', ec='#ff4444', alpha=0.5))

    # Panel B Configuration: OCM Lattice Stability
    ax2.set_facecolor('#090a0f')
    
    # Render structural manifold seams ("beads on a string" visual reference)
    seam_lines = np.linspace(-1.5, 1.5, 5)
    for sl in seam_lines:
        ax2.plot([-3.5, 3.5], [sl * (1.0 - 0.2)] * 2, color='#12253f', linestyle='-', linewidth=0.8, alpha=0.5, zorder=1)
        
    ax2.scatter(solver.x_base, solver.y_base, color='gray', s=12, alpha=0.25, label='Initial Cloud Gas', zorder=2)
    ax2.scatter(xo, yo, color='#45f3ff', s=20, alpha=0.85, edgecolors='#ffffff', linewidths=0.2, label='OCM Locked Family', zorder=5)
    ax2.set_xlim(-4, 4); ax2.set_ylim(-4, 4); ax2.set_aspect('equal'); ax2.axis('off')
    ax2.set_title("OCM Cohesive Nodal Tethering\n(Manifold Viscosity Lattice Lock-in)", color='#45f3ff', fontsize=11, weight='bold')
    ax2.legend(facecolor='#13141f', edgecolor='none', labelcolor='white', loc='lower right')
    
    # Right Telemetry Box
    ax2.text(-3.8, -3.8, f"Mean Separation : {mean_sep_o:.2f} pc\nSpatial Variance: {var_o:.2f}", 
             color='#45f3ff', fontname='monospace', fontsize=9, bbox=dict(boxstyle='round,pad=0.4', fc='#0d0e12', ec='#45f3ff', alpha=0.5))

    # Master Title block
    fig.suptitle("Numerical Integration Comparison: Jeans Fragmentation vs. OCM Structural Bounds", 
                 color='white', fontsize=12, weight='bold')

    # Output directly to your project artifacts root directory
    output_path = 'jeans_instability_comparison.png'
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Success: Analytical comparison graphic generated safely at '{output_path}'.")

if __name__ == '__main__':
    main()
