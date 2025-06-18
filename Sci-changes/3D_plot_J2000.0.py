import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the ecliptic plane using thin grid lines (instead of a surface)
plane_range = 1.2  # in AU

# Draw X and Y axes in the ecliptic plane
ax.quiver(0, 0, 0, 1, 0, 0, color='red', linewidth=2, label='X')
ax.quiver(0, 0, 0, 0, 1, 0, color='green', linewidth=2, label='Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='blue', linewidth=2, label='Z (Ecliptic North)')

# Labels for axes
ax.text(1.1, 0, 0, 'X', color='red', fontsize=10)
ax.text(1.5, 0.001, 0, '(Points toward Vernal Equinox)', color='red', fontsize=8)
ax.text(0, 1.05, 0, 'Y', color='green', fontsize=10)
ax.text(0.03, 0, 1.05, 'Z', color='blue', fontsize=10)

# Optional: draw a small circle to show the ecliptic plane
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
z_circle = np.zeros_like(theta)
ax.plot(x_circle, y_circle, z_circle, color='gray', alpha=0.4, label='Ecliptic Plane')

# Sun at the origin
ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')

# Set viewing angle
ax.view_init(elev=30, azim=60)

# Set limits and aspect
ax.set_xlim([-plane_range, plane_range])
ax.set_ylim([-plane_range, plane_range])
ax.set_zlim([-plane_range, plane_range])
ax.set_box_aspect([1, 1, 1])

# Axis labels
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')

# Title and legend
ax.set_title('J2000 Ecliptic Reference Frame')
ax.legend()

plt.tight_layout()
file_name = "Coordinates.png"
plt.savefig(file_name, bbox_inches="tight", dpi=300)