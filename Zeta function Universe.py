#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Define the density profile for each phase using the zeta function
def density(r, zeta, rho_0=1, lambda_=1):
    return rho_0 * np.maximum(0, 1 + zeta * np.sin(2 * np.pi * r / lambda_))

# Parameters for visualization
r_max = 15  # Maximum radius (arbitrary units, 15 Mpc)
r = np.linspace(0.01, r_max, 100)  # Linear radial grid, increased sampling
theta = np.linspace(0, np.pi, 50)  # Polar angle (0 to pi), increased sampling
phi = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle (0 to 2pi), increased sampling
R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')

# Zeta values for each phase
zetas = [314, 188, 188, 278]  # zeta_1, zeta_2, zeta_3, zeta_4
phase_names = ["Initial Phase (zeta=314)", "First Phase (zeta=188)",
               "Second Phase (zeta=188)", "Third Phase (zeta=278)"]

# Generate a separate 3D and 2D plot for each phase
for i, (zeta, phase_name) in enumerate(zip(zetas, phase_names)):
    # Compute density for the current phase
    Rho = density(R, zeta, rho_0=1, lambda_=1)

    # Normalize density for 3D visualization within this phase only
    Rho_3d = np.nan_to_num(Rho, nan=0.0, posinf=0.0, neginf=0.0)  # Replace inf and nan with 0
    Rho_3d = np.clip(Rho_3d, 0, np.percentile(Rho_3d[np.isfinite(Rho_3d)], 95))  # Cap at 95th percentile
    Rho_3d = Rho_3d / np.max(Rho_3d[Rho_3d > 0])  # Normalize to [0, 1] for this phase

    # Convert spherical to Cartesian coordinates for 3D plotting
    X = R * np.sin(Theta) * np.cos(Phi)
    Y = R * np.sin(Theta) * np.sin(Phi)
    Z = R * np.cos(Theta)

    # Flatten arrays for scatter plot
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    Z_flat = Z.flatten()
    Rho_3d_flat = Rho_3d.flatten()

    # Create a figure with two subplots: 3D on top, 2D on bottom
    fig = plt.figure(figsize=(10, 12))

    # 3D Scatter Plot with viridis colormap
    ax1 = fig.add_subplot(211, projection='3d')
    sc = ax1.scatter(X_flat, Y_flat, Z_flat, c=Rho_3d_flat, cmap=cm.viridis, alpha=0.6, s=20)
    plt.colorbar(sc, ax=ax1, label='Normalized Density (Within Phase)')
    ax1.set_xlabel('X (Mpc)')
    ax1.set_ylabel('Y (Mpc)')
    ax1.set_zlabel('Z (Mpc)')
    ax1.set_title(f'3D Density Distribution - {phase_name}', pad=20)
    ax1.set_box_aspect([1, 1, 1])

    # 2D Radial Plot with Absolute Density
    ax2 = fig.add_subplot(212)
    r_fine = np.linspace(0.01, r_max, 200)
    rho_fine = density(r_fine, zeta, rho_0=1, lambda_=1)
    ax2.plot(r_fine, rho_fine, 'b-', label=f'Absolute Density (zeta = {zeta})')
    ax2.set_xlabel('Radius r (Mpc)')
    ax2.set_ylabel('Absolute Density')
    ax2.set_title(f'2D Radial Density Profile - {phase_name}')
    ax2.grid(True)
    ax2.legend()

    # Adjust layout and save
    plt.tight_layout()

    plt.show()


# In[ ]:




