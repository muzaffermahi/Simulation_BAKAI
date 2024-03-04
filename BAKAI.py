#Muzaffer Mahi Can, 10/02/2024
#Ground assumptions: As the comet moves, it is assumed that in dt the acceleration is constant, as dt gets smaller the calculations are
#slower but more accurate.

import time
import numpy as np
import skyfield
from skyfield.api import load, Topos
from datetime import timedelta


start_time = time.perf_counter() #Starts counting time untill code finishes

ts = load.timescale()
planets = load('de421.bsp') #Load planets positions in the given date

b_date = ts.utc(2013,10, 1) #Beginning date, as simulation runs it starts the date as b_date

dt = 720 #Time that acceleration is assumed to be constant, smaller is better

total_time = 86400*60 #Total simulation time.

#Load planets positions
merkur = planets['mercury barycenter']
venus = planets['venus barycenter']
earth = planets['earth barycenter']
mars = planets['mars barycenter']
jupiter = planets['jupiter barycenter']
saturn = planets['saturn barycenter']
uranus = planets['uranus barycenter']
neptun = planets['neptune barycenter']

#Define position-velocity-acceleraiton vectors for ISON
vctr_position_ISON = np.zeros((int(total_time / dt), 3))
vctr_velocity_ISON = np.zeros((int(total_time / dt), 3))
vctr_acceleration_ISON = np.zeros((int(total_time / dt), 3), dtype=object)

#Define the net distance between objects and ISON
net_distance_mars = np.zeros((int(total_time/dt), 3))
net_distance_earth = np.zeros((int(total_time/dt), 3))
net_distance_jupiter = np.zeros((int(total_time / dt), 3))
net_distance_sun = np.zeros(int(total_time / dt))
net_distance_sun[0] = np.linalg.norm(vctr_position_ISON[0])

#Define the distances of objects to ISON as norm
norm_distance_earth = np.zeros(int(total_time/dt))
norm_distance_mars = np.zeros(int(total_time/dt))

#Beginning position and velocities for ISON
vctr_position_ISON[0] = np.array([-9.847691979997699E+07,2.254323426187314E+08,1.705600566664201E+07])
vctr_velocity_ISON[0] = np.array([1.176261267381250E+01,-3.023110865122838E+01,-4.772431731046794])

#Define constants
G = 0.00000000000000000006674
M_SUN = 1989000000000000000000000000000
M_JUPITER = 1898130000000000000000000000
M_earth = 5972200000000000000000000
M_MARS = 639000000000000000000000

#Create a list to append distances from objects
net_distance_sun_lst = []
net_distance_earth_lst = []
net_distance_mars_lst = []




#Update date and new positions of planets
for i in range(1, int(total_time/864000)):
    b_date += timedelta(days =10)
    merkur_position = merkur.at(b_date).position.km
    venus_position = venus.at(b_date).position.km
    earth_position = earth.at(b_date).position.km
    mars_position = mars.at(b_date).position.km
    jupiter_position = np.array(jupiter.at(b_date).position.km)
    saturn_position = saturn.at(b_date).position.km
    uranus_position = uranus.at(b_date).position.km
    neptun_position = neptun.at(b_date).position.km
    
   #if (G*M_JUPITER*net_distance_jupiter[i]/np.linalg.norm(net_distance_jupiter[i])**3) > 1/10000000000
    net_distance_jupiter[0] = np.array(jupiter_position - vctr_position_ISON[0])
    net_distance_earth[0] = np.array(earth_position - vctr_position_ISON[0])
    net_distance_mars[0] = np.array(mars_position - vctr_position_ISON[0])

    #Calculate positions of ISON and distances from objects for Total Time
    for n in range(1, int(total_time / dt)):
        vctr_acceleration_ISON[n] = (- G * M_SUN* vctr_position_ISON[n-1]/(np.linalg.norm(vctr_position_ISON[n-1])**3)) - G*M_JUPITER*net_distance_jupiter[n-1]/(np.linalg.norm(net_distance_jupiter[n-1])**3) - G*M_earth*net_distance_earth[n-1]/(np.linalg.norm(net_distance_earth[n-1]**3)) - G*M_MARS*net_distance_mars[n-1]/(np.linalg.norm(net_distance_mars[n-1]**3))
        vctr_velocity_ISON[n] = vctr_velocity_ISON[n-1] + vctr_acceleration_ISON[n-1]*dt
        vctr_position_ISON[n] = vctr_position_ISON[n-1] + vctr_velocity_ISON[n-1]*dt + dt**2*vctr_acceleration_ISON[n-1]

        net_distance_jupiter[n] = jupiter_position - vctr_position_ISON[n-1]
        net_distance_earth[n] = earth_position - vctr_position_ISON[n-1]
        net_distance_mars[n] = mars_position - vctr_position_ISON[n-1]

        net_distance_sun[n] = np.linalg.norm(vctr_position_ISON[n])
        net_distance_sun_lst.append(net_distance_sun[n])

        norm_distance_earth[n] = np.linalg.norm(net_distance_earth[n])
        net_distance_earth_lst.append(norm_distance_earth[n])

        norm_distance_mars[n] = np.linalg.norm(net_distance_mars[n])
        net_distance_mars_lst.append(norm_distance_mars[n])
    
#Add values of distances of ISON from objects as arrays
net_distance_sun_arr = np.array(net_distance_sun_lst)
net_distance_earth_arr = np.array(net_distance_earth_lst)
net_distance_mars_arr = np.array(net_distance_mars_lst)

#Choose the smallest distance from sun to obtain perihelion
perihelion = np.min(net_distance_sun_arr)
perihelion_index = np.argmin(net_distance_sun_arr)
t_perihelion = perihelion_index *dt
aphelion = np.max(net_distance_sun_arr)

#Choose the smallest distance from sun
earth_min_distance = np.min(net_distance_earth_arr)
mars_min_distance = np.min(net_distance_mars_arr)

#End time counter
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time: (s)", elapsed_time)
print(f"Last calculated position: {vctr_position_ISON[n]}")
print(f"Last calculated distance from sun: {net_distance_sun[n]}")
print(f"Perihelion during simulation time:{perihelion}")
print(f"Time until perihelion during simulation: {t_perihelion}", end='\n\n')
print(f"earth_acc={G*M_earth/np.linalg.norm(net_distance_earth[0]**2)}" )
print(f"Jupiter_acc={G*M_JUPITER/np.linalg.norm(net_distance_jupiter[0]**2)}")
print(f"sun_acc ={G*M_SUN/(np.linalg.norm(vctr_position_ISON[0])**2)}")

print(f"earth min distance = {earth_min_distance}")
print(f"earth max acc:{G*M_earth/earth_min_distance**2}")

print(f"Mars min distance = {mars_min_distance}")
print(f"Mars max acc = {G*M_MARS/mars_min_distance**2}")

