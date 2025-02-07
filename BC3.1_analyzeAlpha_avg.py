import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Define the data
labels = ["135", "Average of the rest"]
values = [2.497943e+11, 5.125879e+10]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(7, 7))

# Define rectangle properties
bar_width = 0.1

# Plot each value as a rectangle
for i, (label, value) in enumerate(zip(labels, values)):
    rect = patches.Rectangle(
        (i - bar_width / 2, 0),  # Bottom-left corner
        bar_width,  # Width
        value,  # Height
        linewidth=1.75,
        edgecolor='black',
        facecolor='orange'
    )
    ax.add_patch(rect)

# Set axis limits
y_min = 0
y_max = max(values)
ax.set_xlim(-1, len(labels))
ax.set_ylim(y_min, y_max * 1.1)  # Add 10% padding

# Add horizontal grid lines for reference
y_interval = max(20, (y_max - y_min) // 15)
for y in np.arange(y_min, y_max + y_interval, y_interval):
    ax.axhline(y, color='black', linestyle='--', linewidth=0.7, alpha=0.6)

# Customize labels
ax.set_xlabel("Angle Alpha (degrees)", fontsize=16)  # No x-label as per the original style
ax.set_ylabel("Total Earth deviation (km)", fontsize=16)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=12)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

file_name = "BC3.1_Analysis_Alpha_avg.png"
plt.savefig(file_name, bbox_inches="tight", dpi=300)
plt.show()
