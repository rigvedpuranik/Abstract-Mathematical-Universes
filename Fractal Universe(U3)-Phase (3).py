#!/usr/bin/env python
# coding: utf-8

# In[3]:



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

# Functional A: fractal dimension
def fractal_dimension(theta):
    return 7.5+0.9*np.sin(theta)*np.cos(theta)*np.tan(theta)+4.5+0.7*np.cos(theta)+np.sin(theta)

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
             f'D(θ)=7.5+0.9*sin(θ)*cos(θ)*tan(θ)+4.5+0.7*cos(θ)+sin(θ), α={alpha}, t={t_snapshot}', pad=20)

ax.set_box_aspect([1, 1, 1])
plt.savefig(f'u3_fractal_density_3d_alpha{alpha}_t{t_snapshot}.png')
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Functional A: fractal dimension with angular dependence
def fractal_dimension(theta):
    return (7.5 + 0.9*np.sin(theta)*np.cos(theta)*np.tan(theta)) \
           + (4.5 + 0.7*np.cos(theta)**2) + np.sin(theta)

# Functional B: temporal fractional scaling
alpha = 1.2

def density(r, theta, t):
    D = fractal_dimension(theta)
    return (t**(-alpha)) * np.power(r, D - 3)

# Parameters
r_max = 10
r = np.linspace(0.1, r_max, 200)
theta = np.linspace(0, 2*np.pi, 720)
R, Theta = np.meshgrid(r, theta)

# Time snapshot
t_snapshot = 1.0   # try changing to 0.5, 2.0, 5.0, etc.

# Compute density
Rho = density(R, Theta, t_snapshot)

# Handle NaN and Inf from tan(theta) singularities
Rho = np.nan_to_num(Rho, nan=0.0, posinf=0.0, neginf=0.0)

# Normalize for visualization
Rho = np.clip(Rho, 0, np.percentile(Rho, 95))
Rho = Rho / np.max(Rho) if np.max(Rho) > 0 else Rho

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')
c = ax.pcolormesh(Theta, R, Rho, cmap=cm.inferno, shading='auto')
plt.colorbar(c, ax=ax, label='Normalized Density')

ax.contour(Theta, R, Rho, levels=[0.2, 0.5, 0.8],
           colors='white', linestyles='dashed')

ax.set_title(f'Fractal Density Distribution in Universe U3\n'
             f'D(θ) complex form, α={alpha}, t={t_snapshot}', pad=20)
ax.set_xlabel('Assumed Scale: r = 10 → 10 Mpc')
ax.grid(True)

plt.savefig(f'u3_fractal_density_alpha{alpha}_t{t_snapshot}.png', dpi=300)
plt.show()


# In[ ]:




