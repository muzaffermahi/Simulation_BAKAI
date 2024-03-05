# Muzaffer Mahi Can, 10/02/2024

import time
import numpy as np
from skyfield.api import load, Topos
from datetime import timedelta

# Define constants
G = 0.00000000000000000006674
M_SUN = 1989000000000000000000000000000
M_JUPITER = 1898130000000000000000000000
M_EARTH = 5972200000000000000000000
M_MARS = 639000000000000000000000


def print_data():
    print(f"Elapsed time (s): {elapsed_time}")
    print(f"Last calculated position: {vctr_position_ISON[len(vctr_position_ISON) - 1]}")
    print(f"Last calculated distance from sun: {net_distance_sun[len(net_distance_sun) - 1]}")
    print(f"Perihelion during simulation time: {perihelion}")
    print(f"Time until perihelion during simulation: {t_perihelion}\n")
    print(f"earth_acc = {G * M_EARTH / np.linalg.norm(net_distance_earth[0] ** 2)}")
    print(f"Jupiter_acc = {G * M_JUPITER / np.linalg.norm(net_distance_jupiter[0] ** 2)}")
    print(f"sun_acc = {G * M_SUN / (np.linalg.norm(vctr_position_ISON[0]) ** 2)}")

    print(f"earth min distance = {earth_min_distance}")
    print(f"earth max acc: {G * M_EARTH / earth_min_distance ** 2}")

    print(f"Mars min distance = {mars_min_distance}")
    print(f"Mars max acc = {G * M_MARS / mars_min_distance ** 2}")


start_time = time.perf_counter()  # Starts counting time until code finishes

ts = load.timescale()
planets = load('de421.bsp')  # Load planets positions in the given date

b_date = ts.utc(2013, 10, 1)  # Beginning date, as simulation runs it starts the date as b_date

dt = 720  # Time that acceleration is assumed to be constant, smaller is better

total_time = 86400 * 60  # Total simulation time.

# Load planets positions
planets_map = {
    "mercury": planets['mercury barycenter'],
    "venus": planets['venus barycenter'],
    "earth": planets['earth barycenter'],
    "mars": planets['mars barycenter'],
    "jupiter": planets['jupiter barycenter'],
    "saturn": planets['saturn barycenter'],
    "uranus": planets['uranus barycenter'],
    "neptune": planets['neptune barycenter'],
}

# Define position-velocity-acceleration vectors for ISON
vctr_position_ISON = np.zeros((int(total_time / dt), 3))
vctr_velocity_ISON = np.zeros((int(total_time / dt), 3))
vctr_acceleration_ISON = np.zeros((int(total_time / dt), 3), dtype=object)

# Define the net distance between objects and ISON
net_distance_mars = np.zeros((int(total_time / dt), 3))
net_distance_earth = np.zeros((int(total_time / dt), 3))
net_distance_jupiter = np.zeros((int(total_time / dt), 3))
net_distance_sun = np.zeros(int(total_time / dt))
net_distance_sun[0] = np.linalg.norm(vctr_position_ISON[0])

# Define the distances of objects to ISON as norm
norm_distance_earth = np.zeros(int(total_time / dt))
norm_distance_mars = np.zeros(int(total_time / dt))

# Beginning position and velocities for ISON
vctr_position_ISON[0] = np.array([-9.847691979997699E+07, 2.254323426187314E+08, 1.705600566664201E+07])
vctr_velocity_ISON[0] = np.array([1.176261267381250E+01, -3.023110865122838E+01, -4.772431731046794])

# Create a list to append distances from objects
net_distance_sun_lst = []
net_distance_earth_lst = []
net_distance_mars_lst = []

# Update date and new positions of planets
for i in range(1, int(total_time / 864000)):
    b_date += timedelta(days=10)

    planet_locations_map = {}
    for key in planets_map.keys():
        planet_locations_map[key] = planets_map[key].at(b_date).position.km

    net_distance_jupiter[0] = np.array(planet_locations_map["jupiter"] - vctr_position_ISON[0])
    net_distance_earth[0] = np.array(planet_locations_map["earth"] - vctr_position_ISON[0])
    net_distance_mars[0] = np.array(planet_locations_map["mars"] - vctr_position_ISON[0])

    # Calculate positions of ISON and distances from objects for Total Time
    for n in range(1, int(total_time / dt)):
        r_ISON = vctr_position_ISON[n - 1]

        r_jupiter = planet_locations_map["jupiter"]
        r_earth = planet_locations_map["earth"]
        r_mars = planet_locations_map["mars"]

        norm_r_ISON_cubed = np.linalg.norm(r_ISON) ** 3

        acc_ISON = (-G * M_SUN * r_ISON / norm_r_ISON_cubed
                    - G * M_JUPITER * (r_jupiter - r_ISON) / np.linalg.norm(r_jupiter - r_ISON) ** 3
                    - G * M_EARTH * (r_earth - r_ISON) / np.linalg.norm(r_earth - r_ISON) ** 3
                    - G * M_MARS * (r_mars - r_ISON) / np.linalg.norm(r_mars - r_ISON) ** 3)

        vctr_velocity_ISON[n] = vctr_velocity_ISON[n - 1] + acc_ISON * dt

        vctr_position_ISON[n] = (vctr_position_ISON[n - 1] + vctr_velocity_ISON[n - 1] * dt +
                                 0.5 * dt ** 2 * acc_ISON)

        net_distance_jupiter[n] = r_jupiter - vctr_position_ISON[n - 1]
        net_distance_earth[n] = r_earth - vctr_position_ISON[n - 1]
        net_distance_mars[n] = r_mars - vctr_position_ISON[n - 1]

        net_distance_sun[n] = np.linalg.norm(vctr_position_ISON[n])

        net_distance_sun_lst.append(net_distance_sun[n])
        net_distance_earth_lst.append(np.linalg.norm(net_distance_earth[n]))
        net_distance_mars_lst.append(np.linalg.norm(net_distance_mars[n]))

# Add values of distances of ISON from objects as arrays
net_distance_sun_arr = np.array(net_distance_sun_lst)
net_distance_earth_arr = np.array(net_distance_earth_lst)
net_distance_mars_arr = np.array(net_distance_mars_lst)

# Choose the smallest distance from sun to obtain perihelion
perihelion = np.min(net_distance_sun_arr)
perihelion_index = np.argmin(net_distance_sun_arr)
t_perihelion = perihelion_index * dt
aphelion = np.max(net_distance_sun_arr)

# Choose the smallest distance from sun
earth_min_distance = np.min(net_distance_earth_arr)
mars_min_distance = np.min(net_distance_mars_arr)

# End time counter
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print_data()
