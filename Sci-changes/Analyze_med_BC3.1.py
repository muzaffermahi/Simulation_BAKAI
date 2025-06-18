import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Step 1: Load the Data ---
file_path = "dataset_bc3.1.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1", usecols=[
    "Rogue planets speed in Z",
    "Amount earth has deviated because of Rogue"
])

# --- Step 2: Group by velocity and compute median & standard deviation ---
deviation_summary = df.groupby("Rogue planets speed in Z")[
    "Amount earth has deviated because of Rogue"
].agg(['median', 'std']).reset_index()

# Rename for clarity
deviation_summary.columns = ["Z-Velocity (km/s)", "Median Deviation (km)", "Standard Deviation (km)"]

# --- Step 3: Print Summary ---
print("Summary Table:")
print(deviation_summary)

# --- Step 4: Plot Median with Error Bars (Standard Deviation) ---
plt.figure(figsize=(10, 6))
plt.errorbar(
    deviation_summary["Z-Velocity (km/s)"],
    deviation_summary["Median Deviation (km)"],
    yerr=deviation_summary["Standard Deviation (km)"],
    fmt='o',
    color='blue',
    ecolor='black',
    capsize=5,
    markersize=5
)

# Labels and grid
plt.xlabel("Rogue Planet's Initial Z-Velocity (km/s)", fontsize=12)
plt.ylabel("Median Earth Deviation (km)", fontsize=12)
plt.grid(True)

# Custom legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='blue', linestyle='None', markersize=6, label='Median'),
    Line2D([0], [0], marker='|', color='black', markersize=12, linestyle='None', label='SD')
]
plt.legend(handles=legend_elements, loc='best')

# Layout and show
plt.tight_layout()

file_name = "BC1_Median.png"
plt.savefig(file_name, bbox_inches="tight", dpi=300)