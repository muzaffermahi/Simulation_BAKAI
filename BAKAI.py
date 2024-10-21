# Muzaffer Mahi Can, 21/10/2024(I'm getting old), beginning date of the simulation is 16/05

#Long computation, Plug in the values from Big Computation to track for 100 years or so. If your ram gets full, 
#simply decrease total_time x times and increase I_Range x times and it should be fine.

import math
import time 
import numpy as np 
from numba import njit, prange, jit  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import sys
import pandas as pd  
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from math import sin, cos, tan, acos
import csv
import gc
import dask.dataframe as dd 

dt = 144  # Time that acceleration is assumed to be constant, smaller is better

total_time = 86400 * 365.24219/10   # Total simulation time in seconds

n = int(total_time/dt) -1

# Define position-velocity-acceleration vectors for floats

#Positions L
vctr_position_Rogue_L = np.zeros((int(total_time / dt), 3))
vctr_position_earth_L = np.zeros((int(total_time / dt), 3))
vctr_position_moon_L = np.zeros((int(total_time / dt), 3))
vctr_position_earth0_L = np.zeros((int(total_time / dt), 3))
vctr_position_mercury_L = np.zeros((int(total_time / dt), 3))
vctr_position_venus_L = np.zeros((int(total_time / dt), 3))
vctr_position_mars_L = np.zeros((int(total_time / dt), 3))
vctr_position_jupiter_L = np.zeros((int(total_time / dt), 3))
vctr_position_uranus_L = np.zeros((int(total_time / dt), 3))
vctr_position_saturn_L = np.zeros((int(total_time / dt), 3))

#positions F
vctr_position_Rogue_F = np.zeros((int(total_time / dt), 3))
vctr_position_earth_F = np.zeros((int(total_time / dt), 3))
vctr_position_moon_F = np.zeros((int(total_time / dt), 3))
vctr_position_earth0_F = np.zeros((int(total_time / dt), 3))
vctr_position_mercury_F = np.zeros((int(total_time / dt), 3))
vctr_position_venus_F = np.zeros((int(total_time / dt), 3))
vctr_position_mars_F = np.zeros((int(total_time / dt), 3))
vctr_position_jupiter_F = np.zeros((int(total_time / dt), 3))
vctr_position_saturn_F = np.zeros((int(total_time / dt), 3))
vctr_position_uranus_F = np.zeros((int(total_time / dt), 3))

#Velocities L
vctr_velocity_Rogue_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_moon_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth0_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_mercury_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_venus_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_mars_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_jupiter_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_saturn_L = np.zeros((int(total_time / dt), 3))
vctr_velocity_uranus_L = np.zeros((int(total_time / dt), 3))

#Velocities F
vctr_velocity_Rogue_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_moon_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth0_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_mercury_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_venus_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_mars_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_jupiter_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_saturn_F = np.zeros((int(total_time / dt), 3))
vctr_velocity_uranus_F = np.zeros((int(total_time / dt), 3))

#Regular np arrays
vctr_position_earth = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth = np.zeros((int(total_time / dt), 3))
vctr_acceleration_earth = np.zeros((int(total_time / dt), 3))

vctr_position_Rogue = np.zeros((int(total_time / dt), 3))
vctr_velocity_Rogue = np.zeros((int(total_time / dt), 3))
vctr_acceleration_Rogue = np.zeros((int(total_time / dt), 3))

vctr_position_earth0 = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth0 = np.zeros((int(total_time / dt), 3))
vctr_acceleration_earth0 = np.zeros((int(total_time / dt), 3))

vctr_position_moon = np.zeros((int(total_time / dt), 3))
vctr_velocity_moon = np.zeros((int(total_time / dt), 3))
vctr_acceleration_moon = np.zeros((int(total_time / dt), 3))

vctr_position_venus = np.zeros((int(total_time / dt), 3))
vctr_velocity_venus = np.zeros((int(total_time / dt), 3))
vctr_acceleration_venus = np.zeros((int(total_time / dt), 3))

vctr_position_mars = np.zeros((int(total_time / dt), 3))
vctr_velocity_mars = np.zeros((int(total_time / dt), 3))
vctr_acceleration_mars = np.zeros((int(total_time / dt), 3))

vctr_position_mercury = np.zeros((int(total_time / dt), 3))
vctr_velocity_mercury = np.zeros((int(total_time / dt), 3))
vctr_acceleration_mercury = np.zeros((int(total_time / dt), 3))
 
vctr_position_jupiter = np.zeros((int(total_time / dt), 3))
vctr_velocity_jupiter = np.zeros((int(total_time / dt), 3))
vctr_acceleration_jupiter = np.zeros((int(total_time / dt), 3))

vctr_position_saturn = np.zeros((int(total_time / dt), 3))
vctr_velocity_saturn = np.zeros((int(total_time / dt), 3))
vctr_acceleration_saturn = np.zeros((int(total_time / dt), 3))

vctr_position_uranus = np.zeros((int(total_time / dt), 3))
vctr_velocity_uranus = np.zeros((int(total_time / dt), 3))
vctr_acceleration_uranus = np.zeros((int(total_time / dt), 3))

vctr_position_neptune = np.zeros((int(total_time / dt), 3))
vctr_velocity_neptune = np.zeros((int(total_time / dt), 3))
vctr_acceleration_neptune = np.zeros((int(total_time / dt), 3))


vctr_position_earth_L[0] = np.array([-8.720402184155567E+07 , -1.249081082441206E+08 , 3.737986027865112E+04]) #16/05/2024, 00:00
vctr_velocity_earth_L[0] = np.array([2.401992974509115E+01 , -1.707462009431704E+01 ,1.433502989955038E-03]) #16/05/2024, 00:00

vctr_position_earth0_L[0] = np.array([-8.612126415163520E+07 ,-1.243405742161587E+08 , 7.159140121236444E+03])
vctr_velocity_earth0_L[0] = np.array([2.400973596546069E+01 ,-1.706428457849702E+01 , 1.571000011289847E-03])

vctr_position_moon_L[0] = np.array([-8.755507860116081E+07,-1.247124832815350E+08 ,6.257550822596997E+04])
vctr_velocity_moon_L[0] = np.array([2.352284152220006E+01 ,-1.790602303115681E+01 ,-6.028641210510699E-02])

vctr_position_venus_L[0] = np.array([7.849069074392912E+07 , 7.265299941189906E+07 ,-3.555650808009125E+06])
vctr_velocity_venus_L[0] = np.array([-2.380890084283434E+01 ,2.561096385253431E+01 ,1.726117286970316E+00])

vctr_position_mars_L[0] = np.array([1.953483986445647E+08 ,-6.736874568063487E+07 ,-6.203471747638375E+06])
vctr_velocity_mars_L[0] = np.array([8.832622761709738E+00 , 2.496428727288077E+01 , 3.068649504636074E-01])

vctr_position_mercury_L[0] = np.array([3.283076702183335E+07 ,-5.553342431715292E+07 ,-7.572312789214641E+06])
vctr_velocity_mercury_L[0] = np.array([3.173906192910079E+01 ,2.796443627270332E+01 ,6.242827348963988E-01])

vctr_position_saturn_L[0] = np.array([1.378702539351859E+09 ,-4.495863763669394E+08 ,-4.705303265259945E+07])
vctr_velocity_saturn_L[0] = np.array([2.450698198991122E+00 , 9.173615828117882E+00 ,-2.575230772687291E-01])

vctr_position_jupiter_L[0] = np.array([3.994637907080921E+08 , 6.337096433353311E+08 ,-1.156604178375214E+07])
vctr_velocity_jupiter_L[0] = np.array([-1.119982261334915E+01 , 7.589272302166839E+00 , 2.190903787427758E-01])

vctr_position_uranus_L[0] = np.array([1.770839386855791E+09 , 2.333940166600484E+09 ,-1.427331145023417E+07])
vctr_velocity_uranus_L[0] = np.array([5.475445009012557E+00 , 3.798950571261637E+00 , 8.505598433128170E-02])

vctr_position_neptune[0] = np.array([4.466207770156772E+09 ,-2.041946325393501E+08,-9.872340112626548E+07])
vctr_velocity_neptune[0] = np.array([2.126333725507608E-01 , 5.461953774781206E+00 ,-1.175120180469107E-01])

#Define constants
G = 6.674e-20
M_SUN= float(1.989 * 10**30)
M_JUPITER = float(1.89813 * 10**27)
M_earth = float(5.972 * 10**24)
M_MARS = float(6.39 * 10**23)
M_VENUS = float(4.8* 10**24)
M_mercury = float(3.285 * 10**23)
M_SATURN = float(5.683 * 10**26)
M_URANUS = float(8.681 * 10**25)
M_NEPTUNE = float(10**26)
M_Rogue = float(M_earth*300)#increased from m_earth to30*m_earth .... till 300
M_Moon = float(7.34767309 * 10**22)
R_earth = 6371 
R_moon = 1737


Roche_limit_Rogue_Earth = int(R_earth*(2*M_Rogue/M_earth)**(1/3))
Roche_limit_Rogue_Earth_check = False

Roche_limit_Earth_Moon = int(R_moon*(2*M_earth/M_Moon)**(1/3))
Roche_limit_Earth_Moon_check = False

Roche_limit_Rogue_Moon = int(R_moon*(2*M_Rogue/M_Moon)**(1/3))
Roche_limit_Rogue_Moon_check = False
X_Earth = float(-8.720402184155567E+07)
Y_Earth = float(-1.249081082441206E+08)

vctr_earth = (X_Earth**2 + Y_Earth**2)**(1/2)
k = float(math.acos(X_Earth/vctr_earth))

c = int(0)
Alpha_degree = 90
Alpha_Radian = math.radians(Alpha_degree)
sub = 250000
X_sub = float(sub*math.sin(Alpha_Radian))
Y_sub = float(sub*math.cos(Alpha_Radian))

X_Rogue = X_Earth + X_sub 
Y_Rogue = Y_Earth + Y_sub
vctr_Rogue = (X_Rogue**2 + Y_Rogue**2)**(1/2)

first_time = time.perf_counter()
vctr_position_Rogue_L[0] = np.array([X_Rogue, Y_Rogue, 1e+06]) 
vctr_velocity_Rogue_L[0] = np.array([0, 0, -200])

Collision = False
#Calculate positions of Rogue and distances from floats for Total Time

@njit
def compute_position(total_time, dt, G, M_SUN, M_earth, M_VENUS, M_MARS, M_mercury, M_JUPITER, M_SATURN, M_NEPTUNE, M_URANUS, M_Rogue, M_Moon,
                                vctr_position_moon, vctr_velocity_moon, vctr_acceleration_moon, 
                                vctr_position_Rogue, vctr_velocity_Rogue, vctr_acceleration_Rogue, 
                                vctr_position_earth, vctr_velocity_earth, vctr_acceleration_earth,
                                vctr_position_venus, vctr_velocity_venus, vctr_acceleration_venus,
                                vctr_position_mars, vctr_velocity_mars, vctr_acceleration_mars,
                                vctr_position_mercury, vctr_velocity_mercury, vctr_acceleration_mercury,
                                vctr_position_jupiter, vctr_velocity_jupiter, vctr_acceleration_jupiter,
                                vctr_position_saturn, vctr_velocity_saturn, vctr_acceleration_saturn,
                                vctr_position_neptune, vctr_velocity_neptune, vctr_acceleration_neptune,
                                vctr_position_uranus, vctr_velocity_uranus, vctr_acceleration_uranus,
                                vctr_position_earth0, vctr_velocity_earth0, vctr_acceleration_earth0,
                                Roche_limit_Rogue_Moon_check,Roche_limit_Earth_Moon_check ,Roche_limit_Rogue_Earth_check,
                                Roche_limit_Rogue_Moon, Roche_limit_Earth_Moon, Roche_limit_Rogue_Earth,
                                vctr_position_Rogue_F,vctr_position_moon_F,vctr_position_earth_F,
                                vctr_position_mercury_F,vctr_position_venus_F,vctr_position_mars_F,
                                vctr_position_jupiter_F,vctr_position_saturn_F,vctr_position_uranus_F,
                                vctr_velocity_Rogue_F,vctr_velocity_moon_F,vctr_velocity_earth_F,
                                vctr_velocity_mercury_F,vctr_velocity_venus_F,vctr_velocity_mars_F,
                                vctr_velocity_jupiter_F,vctr_velocity_saturn_F,vctr_velocity_uranus_F

                                ): 
                
            
            for n in range(1, int(total_time/(dt) )):
                    
                    vctr_acceleration_Rogue[n] = (- G * M_SUN* vctr_position_Rogue[n-1]/np.linalg.norm(vctr_position_Rogue[n-1])**3
                    - G * M_earth * (vctr_position_Rogue[n-1]-vctr_position_earth[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_earth[n-1]**3)
                    - G * M_Moon* (vctr_position_Rogue[n-1]-vctr_position_moon[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_moon[n-1])**3

                    )
                    vctr_velocity_Rogue[n] = vctr_velocity_Rogue[n-1] + vctr_acceleration_Rogue[n-1]*dt
                    vctr_position_Rogue[n] = vctr_position_Rogue[n-1] + vctr_velocity_Rogue[n-1]*dt + 0.5*dt**2*vctr_acceleration_Rogue[n-1]

                    vctr_acceleration_earth[n] = (
                    - G * M_SUN * vctr_position_earth[n-1]/np.linalg.norm(vctr_position_earth[n-1])**3   
                     - G * M_SATURN *(vctr_position_earth[n-1]-vctr_position_saturn[n-1])/np.linalg.norm(vctr_position_earth[n-1]-vctr_position_saturn[n-1])**3
                    - G * M_Moon* (vctr_position_earth[n-1] - vctr_position_moon[n-1])/np.linalg.norm(vctr_position_earth[n-1] - vctr_position_moon[n-1])**3
                    - G * M_Rogue* (vctr_position_earth[n-1] - vctr_position_Rogue[n-1])/np.linalg.norm(vctr_position_earth[n-1] - vctr_position_Rogue[n-1])**3
                    )

                    vctr_velocity_earth[n] = vctr_velocity_earth[n-1] + vctr_acceleration_earth[n-1]*dt
                    vctr_position_earth[n] = vctr_position_earth[n-1] + vctr_velocity_earth[n-1]*dt + 0.5*dt**2*vctr_acceleration_earth[n-1]

                    vctr_acceleration_moon[n] = (- G * M_SUN * vctr_position_moon[n-1]/np.linalg.norm(vctr_position_moon[n-1])**3
                    - G * M_Rogue* (vctr_position_moon[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_moon[n-1] - vctr_position_Rogue[n-1])**3)
                    - G * M_earth*(vctr_position_moon[n-1] - vctr_position_earth[n-1])/(np.linalg.norm(vctr_position_moon[n-1] - vctr_position_earth[n-1])**3)
                    )
                    vctr_velocity_moon[n] = vctr_velocity_moon[n-1] + vctr_acceleration_moon[n-1]*dt
                    vctr_position_moon[n] = vctr_position_moon[n-1] + vctr_velocity_moon[n-1]*dt + 0.5*dt**2*vctr_acceleration_moon[n-1]

                    vctr_acceleration_earth0[n] = (-G * M_SUN * vctr_position_earth0[n-1]/np.linalg.norm(vctr_position_earth0[n-1])**3
                    - G * M_VENUS * (vctr_position_earth0[n-1]-vctr_position_venus[n-1])/np.linalg.norm(vctr_position_earth0[n-1]-vctr_position_venus[n-1])**3
                    - G * M_MARS * (vctr_position_earth0[n-1]-vctr_position_mars[n-1])/(np.linalg.norm(vctr_position_earth0[n-1]-vctr_position_mars[n-1])**3)
                    - G * M_JUPITER* (vctr_position_earth0[n-1]-vctr_position_jupiter[n-1])/np.linalg.norm(vctr_position_earth0[n-1]-vctr_position_jupiter[n-1])**3)
                    vctr_velocity_earth0[n] = vctr_velocity_earth0[n-1] + vctr_acceleration_earth0[n-1]*dt
                    vctr_position_earth0[n] = vctr_position_earth0[n-1] + vctr_velocity_earth0[n-1]*dt + 0.5*dt**2*vctr_acceleration_earth0[n-1]

                    vctr_acceleration_venus[n] = (- G * M_SUN * vctr_position_venus[n-1]/np.linalg.norm(vctr_position_venus[n-1])**3
                    - G * M_Rogue* (vctr_position_venus[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_venus[n-1] - vctr_position_Rogue[n-1])**3)
                    )
                    vctr_velocity_venus[n] = vctr_velocity_venus[n-1] + vctr_acceleration_venus[n-1]*dt
                    vctr_position_venus[n] = vctr_position_venus[n-1] + vctr_velocity_venus[n-1]*dt + 0.5*dt**2*vctr_acceleration_venus[n-1]

                    vctr_acceleration_mars[n] = (-G * M_SUN * vctr_position_mars[n-1]/np.linalg.norm(vctr_position_mars[n-1])**3
                    - G * M_JUPITER* (vctr_position_mars[n-1]-vctr_position_jupiter[n-1])/np.linalg.norm(vctr_position_mars[n-1]-vctr_position_jupiter[n-1])**3
                    - G * M_Rogue* (vctr_position_mars[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_mars[n-1] - vctr_position_Rogue[n-1])**3))
                    vctr_velocity_mars[n] = vctr_velocity_mars[n-1] + vctr_acceleration_mars[n-1]*dt
                    vctr_position_mars[n] = vctr_position_mars[n-1] + vctr_velocity_mars[n-1]*dt + 0.5*dt**2*vctr_acceleration_mars[n-1]

                    vctr_acceleration_mercury[n] = (-G * M_SUN * vctr_position_mercury[n-1]/np.linalg.norm(vctr_position_mercury[n-1])**3
                    - G * M_Rogue* (vctr_position_mercury[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_mercury[n-1] - vctr_position_Rogue[n-1])**3))
                    vctr_velocity_mercury[n] = vctr_velocity_mercury[n-1] + vctr_acceleration_mercury[n-1]*dt
                    vctr_position_mercury[n] = vctr_position_mercury[n-1] + vctr_velocity_mercury[n-1]*dt + 0.5*dt**2*vctr_acceleration_mercury[n-1]

                    vctr_acceleration_jupiter[n] = (-G * M_SUN * vctr_position_jupiter[n-1]/np.linalg.norm(vctr_position_jupiter[n-1])**3
                    - G * M_SATURN *(vctr_position_jupiter[n-1]-vctr_position_saturn[n-1])/np.linalg.norm(vctr_position_jupiter[n-1]-vctr_position_saturn[n-1])**3
                    - G * M_Rogue * (vctr_position_jupiter[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_jupiter[n-1] - vctr_position_Rogue[n-1])**3))
                    vctr_velocity_jupiter[n] = vctr_velocity_jupiter[n-1] + vctr_acceleration_jupiter[n-1]*dt
                    vctr_position_jupiter[n] = vctr_position_jupiter[n-1] + vctr_velocity_jupiter[n-1]*dt + 0.5*dt**2*vctr_acceleration_jupiter[n-1]

                    if n == int(total_time/dt)-1:
                        vctr_position_Rogue_F[0] = vctr_position_Rogue[n]
                        vctr_position_earth_F[0] = vctr_position_earth[n]
                        vctr_position_moon_F[0] = vctr_position_moon[n]
                        vctr_position_mercury_F[0] = vctr_position_mercury[n]
                        vctr_position_venus_F[0] = vctr_position_venus[n]
                        vctr_position_mars_F[0] = vctr_position_mars[n]
                        vctr_position_jupiter_F[0] = vctr_position_jupiter[n]
                        vctr_position_saturn_F[0] = vctr_position_saturn[n]

                        vctr_velocity_jupiter_F[0] = vctr_velocity_jupiter[n]
                        vctr_velocity_saturn_F[0] = vctr_velocity_saturn[n]
                        vctr_velocity_moon_F[0] = vctr_velocity_moon[n]
                        vctr_velocity_earth_F[0] = vctr_velocity_earth[n]
                        vctr_velocity_mercury_F[0] = vctr_velocity_mercury[n]
                        vctr_velocity_Rogue_F[0] = vctr_velocity_Rogue[n]
                        vctr_velocity_mars_F[0] = vctr_velocity_mars[n]
                        vctr_velocity_venus_F[0] = vctr_velocity_venus[n]

                    
            return vctr_position_earth[n], vctr_position_Rogue[n], vctr_position_moon[n],vctr_position_mercury[n], vctr_position_venus[n], vctr_position_mars[n] ,vctr_position_jupiter[n], vctr_position_saturn[n], vctr_position_Rogue_F[0],vctr_position_moon_F[0],vctr_position_earth_F[0],vctr_position_mercury_F[0],vctr_position_venus_F[0],vctr_position_mars_F[0],vctr_position_jupiter_F[0],vctr_position_saturn_F[0],vctr_position_uranus_F[0],vctr_velocity_Rogue_F[0],vctr_velocity_moon_F[0],vctr_velocity_earth_F[0],vctr_velocity_mercury_F[0],vctr_velocity_venus_F[0],vctr_velocity_mars_F[0],vctr_velocity_jupiter_F[0],vctr_velocity_saturn_F[0],vctr_velocity_uranus_F[0]
csv_file_path = "abotesti.csv"
I_range = 200
for i in range(0, I_range):
    beginning_time = time.perf_counter()
    if i>0:
        vctr_position_moon_L[i] = vctr_position_moon_F[0]
        vctr_position_Rogue_L[i] = vctr_position_Rogue_F[0]
        vctr_position_earth_L[i] = vctr_position_earth_F[0]
        vctr_position_mercury_L[i] = vctr_position_mercury_F[0]
        vctr_position_venus_L[i] = vctr_position_venus_F[0]
        vctr_position_mars_L[i] = vctr_position_mars_F[0]
        vctr_position_jupiter_L[i] = vctr_position_jupiter_F[0]
        vctr_position_saturn_L[i] = vctr_position_saturn_F[0]
        vctr_position_uranus_L[i] = vctr_position_uranus_F[0]

        vctr_velocity_moon_L[i] = vctr_velocity_moon_F[0]
        vctr_velocity_Rogue_L[i] = vctr_velocity_Rogue_F[0]
        vctr_velocity_earth_L[i] = vctr_velocity_earth_F[0]
        vctr_velocity_mercury_L[i] = vctr_velocity_mercury_F[0]
        vctr_velocity_venus_L[i] = vctr_velocity_venus_F[0]
        vctr_velocity_mars_L[i] = vctr_velocity_mars_F[0]
        vctr_velocity_jupiter_L[i] = vctr_velocity_jupiter_F[0]
        vctr_velocity_saturn_L[i] = vctr_velocity_saturn_F[0]
        vctr_velocity_uranus_L[i] = vctr_velocity_uranus_F[0]

    vctr_position_earth[0] = vctr_position_earth_L[i]
    vctr_position_Rogue[0] = vctr_position_Rogue_L[i] 
    vctr_position_moon[0] = vctr_position_moon_L[i]
    vctr_position_mercury[0] = vctr_position_mercury_L[i]
    vctr_position_venus[0] = vctr_position_venus_L[i]
    vctr_position_jupiter[0] = vctr_position_jupiter_L[i] 
    vctr_position_saturn[0] = vctr_position_saturn_L[i]
    vctr_position_uranus[0] = vctr_position_uranus_L[i]

    vctr_velocity_moon[0] = vctr_velocity_moon_L[i] 
    vctr_velocity_Rogue[0] = vctr_velocity_Rogue_L[i]
    vctr_velocity_earth[0] = vctr_velocity_earth_L[i]
    vctr_velocity_mercury[0] = vctr_velocity_mercury_L[i] 
    vctr_velocity_venus[0] = vctr_velocity_venus_L[i]
    vctr_velocity_mars[0] = vctr_velocity_mars_L[i]
    vctr_velocity_jupiter[0] = vctr_velocity_jupiter_L[i] 
    vctr_velocity_saturn[0] = vctr_velocity_saturn_L[i]
    vctr_velocity_uranus[0] = vctr_velocity_uranus_L[i]

    compute_position(total_time, dt, G, M_SUN, M_earth, M_VENUS, M_MARS, M_mercury, M_JUPITER, M_SATURN, M_NEPTUNE, M_URANUS, M_Rogue, M_Moon,
                                vctr_position_moon, vctr_velocity_moon, vctr_acceleration_moon, 
                                vctr_position_Rogue, vctr_velocity_Rogue, vctr_acceleration_Rogue, 
                                vctr_position_earth, vctr_velocity_earth, vctr_acceleration_earth,
                                vctr_position_venus, vctr_velocity_venus, vctr_acceleration_venus,
                                vctr_position_mars, vctr_velocity_mars, vctr_acceleration_mars,
                                vctr_position_mercury, vctr_velocity_mercury, vctr_acceleration_mercury,
                                vctr_position_jupiter, vctr_velocity_jupiter, vctr_acceleration_jupiter,
                                vctr_position_saturn, vctr_velocity_saturn, vctr_acceleration_saturn,
                                vctr_position_neptune, vctr_velocity_neptune, vctr_acceleration_neptune,
                                vctr_position_uranus, vctr_velocity_uranus, vctr_acceleration_uranus,
                                vctr_position_earth0, vctr_velocity_earth0, vctr_acceleration_earth0,
                                Roche_limit_Rogue_Moon_check,Roche_limit_Earth_Moon_check ,Roche_limit_Rogue_Earth_check,
                                Roche_limit_Rogue_Moon, Roche_limit_Earth_Moon, Roche_limit_Rogue_Earth,
                                vctr_position_Rogue_F,vctr_position_moon_F,vctr_position_earth_F,
                                vctr_position_mercury_F,vctr_position_venus_F,vctr_position_mars_F,
                                vctr_position_jupiter_F,vctr_position_saturn_F,vctr_position_uranus_F,
                                vctr_velocity_Rogue_F,vctr_velocity_moon_F,vctr_velocity_earth_F,
                                vctr_velocity_mercury_F,vctr_velocity_venus_F,vctr_velocity_mars_F,
                                vctr_velocity_jupiter_F,vctr_velocity_saturn_F,vctr_velocity_uranus_F
                                )

    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for x in range(len(vctr_position_earth)):
            writer.writerow([
            vctr_position_Rogue[x][0], vctr_position_Rogue[x][1], vctr_position_Rogue[x][2],  # Rogue position
            vctr_position_earth[x][0], vctr_position_earth[x][1], vctr_position_earth[x][2],  # Earth position
            vctr_position_moon[x][0], vctr_position_moon[x][1], vctr_position_moon[x][2],      # Moon position
            vctr_position_mercury[x][0], vctr_position_mercury[x][1], vctr_position_mercury[x][2],      # Moon position
            vctr_position_venus[x][0], vctr_position_venus[x][1], vctr_position_venus[x][2],      # Moon position
            vctr_position_mars[x][0], vctr_position_mars[x][1], vctr_position_mars[x][2],      # Moon position
            vctr_position_jupiter[x][0], vctr_position_jupiter[x][1], vctr_position_jupiter[x][2],      # Moon position
            vctr_position_saturn[x][0], vctr_position_saturn[x][1], vctr_position_saturn[x][2],      # Moon position
        ])

    gc.collect()
    vctr_position_earth[:,-1].fill(0)
    vctr_position_Rogue[:,-1].fill(0)
    vctr_position_moon[:,-1].fill(0) 
    vctr_position_mercury[:,-1].fill(0)
    vctr_position_venus[:,-1].fill(0)
    vctr_position_mars[:,-1].fill(0) 
    vctr_position_jupiter[:,-1].fill(0)
    vctr_position_saturn[:,-1].fill(0)

    vctr_velocity_earth[:,-1].fill(0)
    vctr_velocity_Rogue[:,-1].fill(0)
    vctr_velocity_moon[:,-1].fill(0) 
    vctr_velocity_mercury[:,-1].fill(0)
    vctr_velocity_venus[:,-1].fill(0)
    vctr_velocity_mars[:,-1].fill(0) 
    vctr_velocity_jupiter[:,-1].fill(0)
    vctr_velocity_saturn[:,-1].fill(0)

    vctr_acceleration_earth[:,-1].fill(0)
    vctr_acceleration_Rogue[:,-1].fill(0)
    vctr_acceleration_moon[:,-1].fill(0)
    vctr_acceleration_mercury[:,-1].fill(0)
    vctr_acceleration_venus[:,-1].fill(0)
    vctr_acceleration_mars[:,-1].fill(0) 
    vctr_acceleration_jupiter[:,-1].fill(0)
    vctr_acceleration_saturn[:,-1].fill(0) 

    ending_time = time.perf_counter()
    passed_time = ending_time - beginning_time
    print(f"Remaining Time: {passed_time*(I_range - i)}")
    
p_rogue_x, p_rogue_y, p_rogue_z = [], [], []
p_earth_x, p_earth_y, p_earth_z = [], [], []
p_moon_x, p_moon_y, p_moon_z = [], [], []
p_mercury_x, p_mercury_y, p_mercury_z = [], [], []
p_venus_x, p_venus_y, p_venus_z = [], [], []
p_mars_x, p_mars_y, p_mars_z = [], [], []
p_jupiter_x, p_jupiter_y, p_jupiter_z = [], [], []
p_saturn_x, p_saturn_y, p_saturn_z = [], [], []


df = dd.read_csv(csv_file_path, assume_missing=True)

# Iterate through the file in chunks
def extract_data():
    p_rogue_x = df.iloc[:, 0].to_dask_array(lengths=True)
    p_rogue_y = df.iloc[:, 1].to_dask_array(lengths=True)
    p_rogue_z = df.iloc[:, 2].to_dask_array(lengths=True)
    
    p_earth_x = df.iloc[:, 3].to_dask_array(lengths=True)
    p_earth_y = df.iloc[:, 4].to_dask_array(lengths=True)
    p_earth_z = df.iloc[:, 5].to_dask_array(lengths=True)
    
    p_moon_x = df.iloc[:, 6].to_dask_array(lengths=True)
    p_moon_y = df.iloc[:, 7].to_dask_array(lengths=True)
    p_moon_z = df.iloc[:, 8].to_dask_array(lengths=True)
    
    p_mercury_x = df.iloc[:, 9].to_dask_array(lengths=True)
    p_mercury_y = df.iloc[:, 10].to_dask_array(lengths=True)
    p_mercury_z = df.iloc[:, 11].to_dask_array(lengths=True)
    
    p_venus_x = df.iloc[:, 12].to_dask_array(lengths=True)
    p_venus_y = df.iloc[:, 13].to_dask_array(lengths=True)
    p_venus_z = df.iloc[:, 14].to_dask_array(lengths=True)
    
    p_mars_x = df.iloc[:, 15].to_dask_array(lengths=True)
    p_mars_y = df.iloc[:, 16].to_dask_array(lengths=True)
    p_mars_z = df.iloc[:, 17].to_dask_array(lengths=True)
    
    p_jupiter_x = df.iloc[:, 18].to_dask_array(lengths=True)
    p_jupiter_y = df.iloc[:, 19].to_dask_array(lengths=True)
    p_jupiter_z = df.iloc[:, 20].to_dask_array(lengths=True)
    
    p_saturn_x = df.iloc[:, 21].to_dask_array(lengths=True)
    p_saturn_y = df.iloc[:, 22].to_dask_array(lengths=True)
    p_saturn_z = df.iloc[:, 23].to_dask_array(lengths=True)
    
    return {
        'p_rogue': (p_rogue_x, p_rogue_y, p_rogue_z),
        'p_earth': (p_earth_x, p_earth_y, p_earth_z),
        'p_moon': (p_moon_x, p_moon_y, p_moon_z),
        'p_mercury': (p_mercury_x, p_mercury_y, p_mercury_z),
        'p_venus': (p_venus_x, p_venus_y, p_venus_z),
        'p_mars': (p_mars_x, p_mars_y, p_mars_z),
        'p_jupiter': (p_jupiter_x, p_jupiter_y, p_jupiter_z),
        'p_saturn': (p_saturn_x, p_saturn_y, p_saturn_z)
    }

def Plot3D():
    # Extract the data lazily
    data = extract_data()
    
    # Now compute the necessary values only for plotting
    p_earth_x, p_earth_y, p_earth_z = [d.compute() for d in data['p_earth']]
    p_rogue_x, p_rogue_y, p_rogue_z = [d.compute() for d in data['p_rogue']]
    p_mars_x, p_mars_y, p_mars_z = [d.compute() for d in data['p_mars']]
    p_jupiter_x, p_jupiter_y, p_jupiter_z = [d.compute() for d in data['p_jupiter']]
    p_mercury_x, p_mercury_y, p_mercury_z = [d.compute() for d in data['p_mercury']]
    p_venus_x, p_venus_y, p_venus_z = [d.compute() for d in data['p_venus']]
    p_moon_x, p_moon_y, p_moon_z = [d.compute() for d in data['p_moon']]

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-4e8, 4e8])
    ax.set_ylim([-4e8, 4e8])
    ax.set_zlim([-4e8, 4e8])
    ax.plot(p_earth_x, p_earth_y, p_earth_z, label='Earth')
    ax.plot(p_rogue_x, p_rogue_y, p_rogue_z, label='Rogue Planet', color='brown')
    ax.plot(p_mars_x, p_mars_y, p_mars_z, label='Mars', color='red')
    ax.plot(p_jupiter_x, p_jupiter_y, p_jupiter_z, label='Jupiter', color='tan')
    ax.plot(p_mercury_x, p_mercury_y, p_mercury_z, label='mercury', color='orange')
    ax.plot(p_venus_x, p_venus_y, p_venus_z, label='venus', color='gold')
    ax.plot(p_moon_x, p_moon_y, p_moon_z, label='moon', color='gray')

    ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')
    ax.set_xlabel('X Position (km)')
    ax.set_ylabel('Y Position (km)')
    ax.set_zlabel('Z Position (km)')
    ax.set_title('Solar System and the Rogue Planet Positions Over Time in 3D')
    ax.legend()
    ax.grid(True)

    photo_file_path = "HanedanTesti_photos"
    if not os.path.exists(photo_file_path):
        os.makedirs(photo_file_path)

    file_name = "Apextest.png"
    file_path = os.path.join(photo_file_path, file_name)
    plt.savefig(file_path)
    plt.close()

Plot3D()


def AxVid():
        # Create a figure and axis for the animation
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim([-4e8, 4e8])
        ax.set_ylim([-4e8, 4e8])
        ax.set_zlim([-4e8, 4e8])
        ax.set_xlabel('X Position (km)')
        ax.set_ylabel('Y Position (km)')
        ax.set_zlabel('Z Position (km)')
        ax.set_title('Motion of Rogue Planet, Earth, Jupiter, and the Sun Over Time')

        # Initialize the lines for Earth, Rogue planet, Jupiter, and the Sun
        line_earth, = ax.plot([], [], [], 'b-', label='Earth')
        line_rogue, = ax.plot([], [], [], 'r-', label='Rogue Planet')
        line_jupiter, = ax.plot([], [], [], 'g-', label='Jupiter')
        line_sun, = ax.plot([], [], [], 'y*', label='Sun', markersize=10)
        ax.legend()

        def init():
            line_earth.set_data([], [])
            line_earth.set_3d_properties([])
            line_rogue.set_data([], [])
            line_rogue.set_3d_properties([])
            line_jupiter.set_data([], [])
            line_jupiter.set_3d_properties([])
            line_sun.set_data([], [])
            line_sun.set_3d_properties([])
            return line_earth, line_rogue, line_jupiter, line_sun

        def update(frame):
            line_earth.set_data(p_earth_x[:frame], p_earth_y[:frame])
            line_earth.set_3d_properties(p_earth_z[:frame])
            line_rogue.set_data(p_rogue_x[:frame], p_rogue_y[:frame])
            line_rogue.set_3d_properties(p_earth_z[:frame])
            line_sun.set_data([0], [0])
            line_sun.set_3d_properties([0])
            return line_earth, line_rogue, line_sun

        total_frames = 15 * 10  # 15 seconds at 10 fps

                # Calculate the step size to ensure the whole video is shown from start to finish
        step_size = len(p_earth_x) // total_frames

                # Create the animation with the calculated step size
        ani = FuncAnimation(fig, update, frames=range(0, len(p_earth_x), step_size), init_func=init, blit=True)

                # Save the animation as a .mov file using the QuickTime (qt) writer
        ani.save('HanedanTesti.gif', writer='qt', fps=10)


if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"File '{csv_file_path}' has been deleted.")


def WriteExcel():
    # Mevcut Excel dosyasının varlığını kontrol et ve oku
    excel_file_path = 'HanedanTesti.xlsx'

    if os.path.exists(excel_file_path):
        existing_df = pd.read_excel(excel_file_path)
    else:
        existing_df = pd.DataFrame()

    new_data = {
                        'total simulation time(days)':[total_time/86400],
                        'dt(seconds)':[dt],
                        'Angle Alpha': [Alpha_degree],
                        'Sub' : [sub],
                        'Rogue planets speed in Z' : [-50],
                        'Amount earth has deviated because of Rogue': [np.linalg.norm(vctr_position_earth0[n]-vctr_position_earth[n])],
                        'Roche limit check between Earth and Rogue': [Roche_limit_Rogue_Earth_check],
                        'Roche limit check between Earth and moon': [Roche_limit_Earth_Moon_check],
                        'Roche limit check between Rogue and moon': [Roche_limit_Rogue_Moon_check],
                            }

    new_df = pd.DataFrame(new_data)
                # Mevcut verilerle yeni verileri birleştirin
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)

                # Excel dosyasına yaz
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
                    combined_df.to_excel(writer, index=False)
WriteExcel()

