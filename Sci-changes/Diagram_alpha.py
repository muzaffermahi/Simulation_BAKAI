import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Parameters
alpha_deg = 45
alpha_rad = math.radians(alpha_deg)
sub = 1e6  # Distance from Earth to rogue in XY
Z_Rogue = 1e6  # Rogue is above the ecliptic

# Earth at origin
X_Earth, Y_Earth = 0, 0

# Rogue planet position in x-y based on alpha
X_sub = sub * np.sin(alpha_rad)
Y_sub = sub * np.cos(alpha_rad)
X_Rogue = X_Earth + X_sub
Y_Rogue = Y_Earth + Y_sub

# --- 3D Plot ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Earth at origin
ax.scatter(0, 0, 0, color='blue', s=80, label='Earth')
ax.scatter(-0.75e6, -0.75e6, 0, color='yellow', s=80, label='Sun')

ax.quiver(-0.75e6, -0.75e6, 0, 0, 1.5e6, 0, color='green', linewidth=2, label='Y')
scale_factor = 1  # Smaller arrow (e.g., 30% length)
ax.quiver(
    X_sub, Y_sub, 0,                 # Start point (rogue's projection)
    -X_sub * scale_factor,          # Δx (toward Earth)
    -Y_sub * scale_factor,          # Δy
    0,                              # Δz (in-plane)
    color='orange',
    linewidth=1,
    arrow_length_ratio=0.15,        # Smaller arrowhead
    normalize=False
)

ax.plot(
    [0,-0.75e6],[0,-0.75e6],[0,0],
    color='orange',
    linestyle = 'dotted',
    linewidth=1,
)

# Rogue planet
ax.scatter(X_Rogue, Y_Rogue, Z_Rogue, color='red', s=80, label='Rogue Planet')
ax.text(-0.75e6, 0.8e6, 0, 'Y', color='green', fontsize=13)

ax.text(0.2e6, -1e5, 0,'Subtraction Vector', color='orange', rotation= -90, fontsize=11)

# Projection onto ecliptic plane (dotted line from rogue to XY)
ax.plot([X_Rogue, X_Rogue], [Y_Rogue, Y_Rogue], [0, Z_Rogue], color='black', linestyle='dotted', label='Z Projection')
ax.scatter(X_Rogue, Y_Rogue, 0, color='gray', s=50, label='Projected Position (XY)')

# Arc showing Alpha
theta_arc = np.linspace(0, alpha_rad, 100)
arc_r = 2.5e5
arc_x = -0.75e6 + arc_r * np.sin(theta_arc)
arc_y = -0.75e6 + arc_r * np.cos(theta_arc)
arc_z = np.zeros_like(arc_x)
ax.plot(arc_x, arc_y, arc_z, color='purple', linewidth=2, label='α')
ax.text(-0.64e6, -0.5e6, 0, f"α", fontsize=12, color='purple')

# Ecliptic plane
plane_size = 1.2e6
xx, yy = np.meshgrid(np.linspace(-plane_size, plane_size, 2),
                     np.linspace(-plane_size, plane_size, 2))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.08, color='orange')

# Axis settings
ax.set_xlim(-1e6, 1e6)
ax.set_ylim(-1e6, 1e6)
ax.set_zlim(0, 1.2e6)
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.legend()
plt.tight_layout()
file_name = "Alpha_visual.png"
plt.savefig(file_name, bbox_inches="tight", dpi=300)