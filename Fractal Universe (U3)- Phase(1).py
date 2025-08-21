#!/usr/bin/env python
# coding: utf-8
#3D Graph
# In[1]:
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Functional A: fractal dimension
def fractal_dimension(theta):
    return 2.5 + 0.5 * np.sin(theta)

# Functional B: temporal scaling with alpha
alpha = 1.2  # fractional temporal order

# Density with time evolution
def density(r, theta, t):
    D = fractal_dimension(theta)
    return (t**(-alpha)) * np.power(r, D - 3)

# Parameters
r_max = 15
r = np.logspace(-2, np.log10(r_max), 30)
theta = np.linspace(0, np.pi, 30)
phi = np.linspace(0, 2*np.pi, 60)
R, Theta, Phi = np.meshgrid(r, theta, phi, indexing='ij')

# Choose a cosmic time snapshot
t_snapshot = 1.0  # can vary (e.g., 0.1, 1, 5)

# Compute density
Rho = density(R, Theta, t_snapshot)

# Clean & normalize
Rho = np.nan_to_num(Rho, nan=0.0, posinf=0.0, neginf=0.0)
Rho = np.clip(Rho, 0, np.percentile(Rho[np.isfinite(Rho)], 95))
Rho = Rho / np.max(Rho[Rho > 0])

# Convert spherical to Cartesian
X = R * np.sin(Theta) * np.cos(Phi)
Y = R * np.sin(Theta) * np.sin(Phi)
Z = R * np.cos(Theta)

# Flatten arrays
X, Y, Z, Rho = [arr.flatten() for arr in (X, Y, Z, Rho)]

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(X, Y, Z, c=Rho, cmap=cm.inferno, alpha=0.6, s=30)
plt.colorbar(sc, ax=ax, label='Normalized Density')

ax.set_xlabel('X (Mpc)')
ax.set_ylabel('Y (Mpc)')
ax.set_zlabel('Z (Mpc)')
ax.set_title(f'Fractal Density Evolution in Universe U3\n'
             f'D(θ)=2.5+0.5sinθ, α={alpha}, t={t_snapshot}', pad=20)

ax.set_box_aspect([1, 1, 1])
plt.savefig(f'u3_fractal_density_3d_alpha{alpha}_t{t_snapshot}.png')
plt.show()



#2D heatmap Graph

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Functional A: fractal dimension
def fractal_dimension(theta):
    return 2.5 + 0.5 * np.sin(theta)

# Functional B: temporal scaling with alpha
alpha = 1.2  # fractional temporal order

# Density profile with time evolution
def density(r, theta, t):
    D = fractal_dimension(theta)
    return (t**(-alpha)) * np.power(r, D - 3)

# Parameters for the visualization
r_max = 10  # Maximum radius (arbitrary units, assume 10 Mpc)
r = np.linspace(0.1, r_max, 200)   # Avoid r=0
theta = np.linspace(0, 2 * np.pi, 720)  # Angular resolution
R, Theta = np.meshgrid(r, theta)

# Choose a cosmic time snapshot
t_snapshot = 1.0   # Try 0.5, 1, 5, etc.

# Compute density for each (r, theta, t)
Rho = density(R, Theta, t_snapshot)

# Normalize density for visualization
Rho = np.nan_to_num(Rho, nan=0.0, posinf=0.0, neginf=0.0)
Rho = np.clip(Rho, 0, np.percentile(Rho, 95))  # Cap at 95th percentile
Rho = Rho / np.max(Rho)  # Normalize to [0, 1]

# Create a polar plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')
c = ax.pcolormesh(Theta, R, Rho, cmap=cm.inferno, shading='auto')

# Add colorbar
plt.colorbar(c, ax=ax, label='Normalized Density')

# Add contour lines
ax.contour(Theta, R, Rho, levels=[0.2, 0.5, 0.8],
           colors='white', linestyles='dashed')

# Title includes alpha and time
ax.set_title(f'Fractal Density in Universe U3\n'
             f'D(θ) = 2.5 + 0.5·sinθ, α={alpha}, t={t_snapshot}', pad=20)

ax.set_xlabel('Assumed Scale: r = 10 → 10 Mpc')
ax.grid(True)

# Save figure
plt.savefig(f'u3_fractal_density_alpha{alpha}_t{t_snapshot}.png', dpi=300)
plt.show()



# In[ ]:




