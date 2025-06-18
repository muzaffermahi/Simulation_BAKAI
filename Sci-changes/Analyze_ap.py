import numpy as np

# Load the data
data = np.loadtxt("Degrees.csv", delimiter=",", skiprows=1)  # skip header if present
angles = data[:, 0]
distances = data[:, 1]

# Lists to store results
perihelion_angles = []
perihelion_distances = []

aphelion_angles = []
aphelion_distances = []

# Detect local minima and maxima
for i in range(1, len(distances) - 1):
    if distances[i - 1] > distances[i] < distances[i + 1]:
        perihelion_angles.append(angles[i])
        perihelion_distances.append(distances[i])
    elif distances[i - 1] < distances[i] > distances[i + 1]:
        aphelion_angles.append(angles[i])
        aphelion_distances.append(distances[i])

# Display counts
print(f"Found {len(perihelion_angles)} perihelion(s) and {len(aphelion_angles)} aphelion(s).\n")

# Print all orbits (only match pairs)
for idx, ((peri_angle, peri_dist), (ap_angle, ap_dist)) in enumerate(zip(
        zip(perihelion_angles, perihelion_distances),
        zip(aphelion_angles, aphelion_distances))):
    
    e = (ap_dist - peri_dist) / (ap_dist + peri_dist)
    a = (ap_dist + peri_dist)/(2* 149597871)
    p = a**(3/2)
    print(f"Orbit {idx+1}:")
    print(f"  Perihelion → angle: {peri_angle:.2f}°, distance: {peri_dist:.2e} km")
    print(f"  Aphelion  → angle: {ap_angle:.2f}°, distance: {ap_dist:.2e} km")
    print(f"Semi-Major Axis: {a} AU")
    print(f"  Eccentricity: {e:.4f}\n")
    print(f"Period: {p} years")
