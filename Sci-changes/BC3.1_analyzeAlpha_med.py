import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Step 1: Load the Data ---
file_path = "dataset_bc3.1.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1", usecols=[
    "Angle Alpha", "Amount earth has deviated because of Rogue"
])

# --- Step 2: Group by Angle Alpha and compute statistics ---
deviation_summary = df.groupby("Angle Alpha")[
    "Amount earth has deviated because of Rogue"
].agg(['median', 'std']).reset_index()

# Rename columns for clarity
deviation_summary.columns = ["Angle Alpha (deg)", "Median Deviation (km)", "Standard Deviation (km)"]

# Print median and SD for each angle
print("\n--- Median and Standard Deviation of Earth Deviation by Angle Alpha ---")
for index, row in deviation_summary.iterrows():
    print(f"Angle: {row['Angle Alpha (deg)']:>6.1f}° | Median: {row['Median Deviation (km)']:.2e} km | SD: {row['Standard Deviation (km)']:.2e} km")
    

average_median_deviation = deviation_summary["Median Deviation (km)"].mean()
print(f"\n--- Overall Average of Median Earth Deviation: {average_median_deviation:.2e} km ---")

# Optional: downsample if data is too large
if len(deviation_summary) > 500:
    deviation_summary = deviation_summary.sample(500)

# Sort data by angle for a clean plot
deviation_summary.sort_values("Angle Alpha (deg)", inplace=True)

# --- Step 3: Scale values to 10^8 km ---
deviation_summary["Median Deviation (km)"] /= 1e8
deviation_summary["Standard Deviation (km)"] /= 1e8
average_median_deviation_scaled = average_median_deviation / 1e8 # Scale the average as well

# --- Step 4: Plot ---
fig, ax = plt.subplots(figsize=(10, 7))

ax.errorbar(
    deviation_summary["Angle Alpha (deg)"],
    deviation_summary["Median Deviation (km)"],
    yerr=deviation_summary["Standard Deviation (km)"],
    fmt='o',
    ecolor='gray',
    capsize=4,
    markersize=5,
    color='blue',
    label="Earth Deviation"
)
ax.axhline(
    average_median_deviation_scaled,
    color='red',
    linestyle='--',
    linewidth=1,
    label=f"Overall Average Median Deviation ({average_median_deviation:.2e} km)"
)
# Axis labels, title, ticks
ax.set_xlabel("Angle Alpha (degrees)", fontsize=14)
ax.set_ylabel("Median Earth Deviation ($10^8$ km)", fontsize=14)
ax.set_title("Earth Deviation vs Angle Alpha", fontsize=16)

# Grid and axis lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Ticks formatting
ax.set_xticks(np.arange(0, 361, 45))
ax.tick_params(axis='x', rotation=20, labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Custom Y-axis ticks: 0 to 10 in steps of 2
y_ticks = np.arange(-19, 30 + 1, 2)
ax.set_yticks(y_ticks)

# Grid and axis lines
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Optional: slightly increase y-axis limit to avoid clipping error bars
ax.set_ylim(-19, 30)
ax.set_xlim(0, 360)

# Legend
ax.legend()

# Save and show plot
plt.tight_layout()
plt.savefig("BC3.1_Alpha_Median_SD_Plot_avg.png", dpi=300)
plt.show()
