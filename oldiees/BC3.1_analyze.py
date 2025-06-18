import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Load only necessary columns to reduce memory usage
file_path = "dataset_bc3.1.xlsx"  
df = pd.read_excel(file_path, sheet_name="Sheet1", usecols=["Rogue planets speed in Z", "Amount earth has deviated because of Rogue"])

# Group by velocity and sum deviation amounts
deviation_summary = df.groupby("Rogue planets speed in Z")["Amount earth has deviated because of Rogue"].sum().reset_index()

# Display summarized results
print(deviation_summary)  # Print only first few rows

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Get x-axis and y-axis ranges
x_min = deviation_summary["Rogue planets speed in Z"].min()
x_max = deviation_summary["Rogue planets speed in Z"].max()
y_min = 0
y_max = deviation_summary["Amount earth has deviated because of Rogue"].max()

# **Limit the number of horizontal lines to avoid memory overload**
y_interval = max(20, (y_max - y_min) // 15)  # At most 15 lines to prevent excessive rendering

# Define width of each rectangle
bar_width = 3  

# **Limit the number of bars drawn** (Optional)
if len(deviation_summary) > 500:
    deviation_summary = deviation_summary.sample(500)  # Random sample of 500 points to reduce overload

# Plot each deviation amount as a rectangle
for _, row in deviation_summary.iterrows():
    x = row["Rogue planets speed in Z"]
    y = row["Amount earth has deviated because of Rogue"]
    
    # Create a rectangle centered at x
    rect = patches.Rectangle(
        (x - bar_width / 2, 0),  # Bottom-left corner
        bar_width,  # Width
        y,  # Height
        linewidth=1.5,
        edgecolor='black',
        facecolor='orange'
    )
    ax.add_patch(rect)

# Add **only a limited number** of horizontal lines
for y in np.arange(y_min, y_max + y_interval, y_interval):
    ax.axhline(y, color='black', linestyle='--', linewidth=0.7, alpha=0.6)

# Customize labels
ax.set_xlabel("Rogue Planet's Speed in Z (km/s)", fontsize = 16)
ax.set_ylabel("Total Earth Deviation (km)", fontsize = 16)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Set limits
ax.set_xlim(x_min - 5, x_max + 5)
ax.set_ylim(y_min, y_max * 1.1)  # Extra 10% padding

# Set x-axis ticks at intervals of 10
ax.set_xticks(np.arange(x_min, x_max + 1, 10))
plt.xticks(rotation=20, fontsize=12)

# Save and show the plot
file_name = "BC3.1_Analysis.png"
plt.savefig(file_name, bbox_inches="tight", dpi=300)
