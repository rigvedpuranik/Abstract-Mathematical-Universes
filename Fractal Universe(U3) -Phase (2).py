#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Define the fractal dimension as a function of theta
def fractal_dimension(theta):
    return 4.5+0.7*np.sin(theta)+ (2.5 +0.5 * np.cos(theta))

# Define the density profile: rho(r, theta, phi) = r^(D(theta, phi) - 3)
def density(r, theta):
    D = fractal_dimension(theta)
    return np.power(r, D - 3)

# Parameters for the 3D visualization
r_max = 15  # Maximum radius (arbitrary units, assumed 5 Mpc)
r = np.logspace(-2, np.log10(r_max), 30)  # Logarithmic radial grid, start from 0.01
theta = np.linspace(0, np.pi, 30)  # Polar angle (0 to pi)
phi = np.linspace(0, 2 * np.pi, 60)  # Azimuthal angle (0 to 2pi)
R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')

# Compute density
Rho = density(R, Theta)

# Normalize density for visualization, handle infinities and NaNs
Rho = np.nan_to_num(Rho, nan=0.0, posinf=0.0, neginf=0.0)  # Replace inf and nan with 0
Rho = np.clip(Rho, 0, np.percentile(Rho[np.isfinite(Rho)], 95))  # Cap at 95th percentile
Rho = Rho / np.max(Rho[Rho > 0])  # Normalize to [0, 1], avoid division by zero

# Convert spherical to Cartesian coordinates for 3D plotting
X = R * np.sin(Theta) * np.cos(Phi)
Y = R * np.sin(Theta) * np.sin(Phi)
Z = R * np.cos(Theta)

# Flatten arrays for scatter plot
X = X.flatten()
Y = Y.flatten()
Z = Z.flatten()
Rho = Rho.flatten()

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with density as color and alpha
sc = ax.scatter(X, Y, Z, c=Rho, cmap=cm.inferno, alpha=0.6, s=30)

# Add a colorbar
plt.colorbar(sc, ax=ax, label='Normalized Density')

# Set labels and title
ax.set_xlabel('X (Mpc)')
ax.set_ylabel('Y (Mpc)')
ax.set_zlabel('Z (Mpc)')
ax.set_title('3D Fractal Density Distribution in Universe U3\nD(θ) = (4.5 + 0.7 * sin(θ)+ 2.5 +0.5 * np.cos(θ)), α = 1.2 (Singular Beginning)', pad=20)

# Set equal aspect ratio (approximate)
ax.set_box_aspect([1, 1, 1])

# Save the plot
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Define the fractal dimension as a function of theta
def fractal_dimension(theta):
    return 4.5+0.7*np.sin(theta)+ (2.5 +0.5 * np.cos(theta))
# Define the density profile: rho(r, theta) = r^(D(theta) - 3)
def density(r, theta):
    D = fractal_dimension(theta)
    return np.power(r, D - 3)

# Parameters for the visualization
r_max = 10  # Maximum radius in arbitrary units (assumed as 10 Mpc for context)
r = np.linspace(0.1, r_max, 200)  # Higher resolution, avoid r=0
theta = np.linspace(0, 2 * np.pi, 720)  # Higher resolution
R, Theta = np.meshgrid(r, theta)

# Compute density for each (r, theta)
Rho = density(R, Theta)

# Normalize density for visualization
Rho = np.clip(Rho, 0, np.percentile(Rho, 95))  # Cap at 95th percentile, ensure non-negative
Rho = Rho / np.max(Rho)  # Normalize to [0, 1]

# Create a polar plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')
c = ax.pcolormesh(Theta, R, Rho, cmap=cm.inferno, shading='auto')
plt.colorbar(c, ax=ax, label='Normalized Density')
ax.contour(Theta, R, Rho, levels=[0.2, 0.5, 0.8], colors='white', linestyles='dashed')
ax.set_title('Fractal Density Distribution in Universe U3\nD(θ) =(4.5 + 0.7 * sin(θ)+ 2.5 +0.5 * np.cos(θ)) and α = 1.2 ' , pad=20)
ax.set_xlabel('Assumed Scale: r = 10 corresponds to 10 Mpc')
ax.grid(True)

# Save the plot
plt.savefig('u3_fractal_density_improved.png')


# In[ ]:




