# Muzaffer Mahi Can, 23/09/2024(I'm getting old), beginning date of the simulation is 16/05

#What's the minimum distance a Rogue Planet can get close to earth so that moon doesn't get ejected or idk man

# Values that are independent: 
# Sub, starts from 5e+5, 1e+06,1.5e+06, 2e+06 .. 1e+07
# Alpha, for every sub it's 0, 90, 180 and 270
import math
import time 
import numpy as np 
from numba import njit, prange  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import sys
import pandas as pd  
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
from math import sin, cos, tan, acos

start_time = time.perf_counter() # Starts counting time untill code finishes

dt = 720  # Time that acceleration is assumed to be constant, smaller is better

total_time = 86400 * 365.24219   # Total simulation time in seconds

n = int(total_time/dt) -1

# Define position-velocity-acceleraiton vectors for floats
vctr_position_Rogue = np.zeros((int(total_time / dt), 3))
vctr_velocity_Rogue = np.zeros((int(total_time / dt), 3))
vctr_acceleration_Rogue = np.zeros((int(total_time / dt), 3))

vctr_position_earth = np.zeros((int(total_time / dt), 3))
vctr_velocity_earth = np.zeros((int(total_time / dt), 3))
vctr_acceleration_earth = np.zeros((int(total_time / dt), 3))

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


vctr_position_earth[0] = np.array([-8.720402184155567E+07 , -1.249081082441206E+08 , 3.737986027865112E+04]) #16/05/2024, 00:00
vctr_velocity_earth[0] = np.array([2.401992974509115E+01 , -1.707462009431704E+01 ,1.433502989955038E-03]) #16/05/2024, 00:00

X_Earth = float(-8.720402184155567E+07)
Y_Earth = float(-1.249081082441206E+08)

vctr_earth = (X_Earth**2 + Y_Earth**2)**(1/2)
k = float(math.acos(X_Earth/vctr_earth))

c = int(0)
for D in range(1, 2):
    Alpha_degree = 0 + D*90
    Alpha_Radian = math.radians(Alpha_degree)
    for S in range(1, 2):
        sub = 0.5E+06 + S * 0.5E+06
        X_sub = float(sub*math.sin(Alpha_Radian))
        Y_sub = float(sub*math.cos(Alpha_Radian))

        X_Rogue = X_Earth + X_sub 
        Y_Rogue = Y_Earth + Y_sub
        vctr_Rogue = (X_Rogue**2 + Y_Rogue**2)**(1/2)

        for V in range(1 , 2):

            print(f"Percent calculated:{c/1600*100}")
            c += 1
            vctr_position_Rogue[0] = np.array([X_Rogue, Y_Rogue, 1e+06]) 
            vctr_velocity_Rogue[0] = np.array([0, 0, (-10 -V*10)])

            vctr_position_earth0[0] = np.array([-8.612126415163520E+07 ,-1.243405742161587E+08 , 7.159140121236444E+03])
            vctr_velocity_earth0[0] = np.array([2.400973596546069E+01 ,-1.706428457849702E+01 , 1.571000011289847E-03])

            vctr_position_moon[0] = np.array([-8.755507860116081E+07,-1.247124832815350E+08 ,6.257550822596997E+04])
            vctr_velocity_moon[0] = np.array([2.352284152220006E+01 ,-1.790602303115681E+01 ,-6.028641210510699E-02])

            vctr_position_venus[0] = np.array([7.849069074392912E+07 , 7.265299941189906E+07 ,-3.555650808009125E+06])
            vctr_velocity_venus[0] = np.array([-2.380890084283434E+01 ,2.561096385253431E+01 ,1.726117286970316E+00])

            vctr_position_mars[0] = np.array([1.953483986445647E+08 ,-6.736874568063487E+07 ,-6.203471747638375E+06])
            vctr_velocity_mars[0] = np.array([8.832622761709738E+00 , 2.496428727288077E+01 , 3.068649504636074E-01])

            vctr_position_mercury[0] = np.array([3.283076702183335E+07 ,-5.553342431715292E+07 ,-7.572312789214641E+06])
            vctr_velocity_mercury[0] = np.array([3.173906192910079E+01 ,2.796443627270332E+01 ,6.242827348963988E-01])

            vctr_position_saturn[0] = np.array([1.378702539351859E+09 ,-4.495863763669394E+08 ,-4.705303265259945E+07])
            vctr_velocity_saturn[0] = np.array([2.450698198991122E+00 , 9.173615828117882E+00 ,-2.575230772687291E-01])

            vctr_position_jupiter[0] = np.array([3.994637907080921E+08 , 6.337096433353311E+08 ,-1.156604178375214E+07])
            vctr_velocity_jupiter[0] = np.array([-1.119982261334915E+01 , 7.589272302166839E+00 , 2.190903787427758E-01])

            vctr_position_uranus[0] = np.array([1.770839386855791E+09 , 2.333940166600484E+09 ,-1.427331145023417E+07])
            vctr_velocity_uranus[0] = np.array([5.475445009012557E+00 , 3.798950571261637E+00 , 8.505598433128170E-02])

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
                                Roche_limit_Rogue_Moon, Roche_limit_Earth_Moon, Roche_limit_Rogue_Earth
                                ): 
                
                min_distance = float('inf')
                min_distance_Earth_moon = float('inf')
                min_distance_Rogue_moon = float('inf')
                max_distance_Earth_moon = int(0)
                for n in range(1, int(total_time/dt )):
                    #print(f"%{int(n/int(total_time/dt)*100)}")
                    vctr_acceleration_Rogue[n] = (- G * M_SUN* vctr_position_Rogue[n-1]/np.linalg.norm(vctr_position_Rogue[n-1])**3
                    - G * M_earth * (vctr_position_Rogue[n-1]-vctr_position_earth[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_earth[n-1]**3)
                    - G * M_VENUS * (vctr_position_Rogue[n-1]-vctr_position_venus[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_venus[n-1])**3
                    - G * M_MARS * (vctr_position_Rogue[n-1]-vctr_position_mars[n-1])/(np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_mars[n-1])**3)
                    - G * M_mercury * (vctr_position_Rogue[n-1]-vctr_position_mercury[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_mercury[n-1])**3
                    - G * M_JUPITER* (vctr_position_Rogue[n-1]-vctr_position_jupiter[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_jupiter[n-1])**3
                    - G * M_Moon* (vctr_position_Rogue[n-1]-vctr_position_moon[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_moon[n-1])**3

                    )
                    vctr_velocity_Rogue[n] = vctr_velocity_Rogue[n-1] + vctr_acceleration_Rogue[n-1]*dt
                    vctr_position_Rogue[n] = vctr_position_Rogue[n-1] + vctr_velocity_Rogue[n-1]*dt + 0.5*dt**2*vctr_acceleration_Rogue[n-1]

                    vctr_acceleration_earth[n] = (
                    - G * M_SUN * vctr_position_earth[n-1]/np.linalg.norm(vctr_position_earth[n-1])**3   
                    - G * M_mercury*(vctr_position_earth[n-1] - vctr_position_mercury[n-1])/np.linalg.norm(vctr_position_earth[n-1] - vctr_position_mercury[n-1])**3
                    - G * M_VENUS * (vctr_position_earth[n-1]-vctr_position_venus[n-1])/np.linalg.norm(vctr_position_earth[n-1]-vctr_position_venus[n-1])**3
                    - G * M_MARS * (vctr_position_earth[n-1]-vctr_position_mars[n-1])/(np.linalg.norm(vctr_position_earth[n-1]-vctr_position_mars[n-1])**3)
                    - G * M_JUPITER* (vctr_position_earth[n-1]-vctr_position_jupiter[n-1])/np.linalg.norm(vctr_position_earth[n-1]-vctr_position_jupiter[n-1])**3
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
                    - G * M_Rogue* (vctr_position_venus[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_venus[n-1] - vctr_position_Rogue[n-1])**3))
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

                    # Calculate the current distance between Earth and the Rogue planet
                    current_distance_Rogue_Earth = np.linalg.norm(vctr_position_earth[n] - vctr_position_Rogue[n])
                    current_distance_Rogue_moon = np.linalg.norm(vctr_position_Rogue[n] - vctr_position_moon[n])
                    """ifcurrent_distance_Rogue_Earth < 100000:
                        dt = 10
                    elifcurrent_distance_Rogue_Earth > 10000000:
                        dt = 7200

                    else: 
                    current_distance_Rogue_Earth = 720"""
                    
                    if Roche_limit_Earth_Moon_check == False:
                        if (np.linalg.norm(vctr_position_earth[n-1] - vctr_position_moon[n-1]) < Roche_limit_Earth_Moon):
                            Roche_limit_Earth_Moon_check = True

                    if Roche_limit_Rogue_Moon_check == False:
                        if (current_distance_Rogue_moon < Roche_limit_Rogue_Moon):
                            Roche_limit_Rogue_Moon_check = True

                    
                    # Update min_distance if the current distance is smaller
                    if current_distance_Rogue_Earth < min_distance:
                        min_distance =current_distance_Rogue_Earth

                    current_distance_Earth_moon = np.linalg.norm(vctr_position_earth[n-1] - vctr_position_moon[n-1])

                    if current_distance_Earth_moon < min_distance_Earth_moon:
                        min_distance_Earth_moon = current_distance_Earth_moon

                    if current_distance_Rogue_moon < min_distance_Rogue_moon:
                        min_distance_Rogue_moon = current_distance_Rogue_moon

                    if current_distance_Earth_moon > max_distance_Earth_moon:
                        max_distance_Earth_moon = current_distance_Earth_moon

                return min_distance, min_distance_Earth_moon, min_distance_Rogue_moon, max_distance_Earth_moon


                
            min_distance_Rogue_moon_global, min_distance_Earth_moon_global , min_distance_global , max_distance_Earth_moon_global = compute_position(
                                total_time, dt, G, M_SUN, M_earth, M_VENUS, M_MARS, M_mercury, 
                                M_JUPITER, M_SATURN, M_NEPTUNE, M_URANUS, M_Rogue, M_Moon,
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
                                Roche_limit_Rogue_Moon, Roche_limit_Earth_Moon, Roche_limit_Rogue_Earth
                                )



            if (min_distance_global < Roche_limit_Rogue_Earth):
                Roche_limit_Rogue_Earth_check = True



            #End time counter
            end_time = time.perf_counter()

            def SmallAx():
                fig = plt.figure(figsize=(10, 10))
                ax = fig.add_subplot(111, projection='3d')
                ax.plot(vctr_position_earth[:, 0], vctr_position_earth[:, 1], vctr_position_earth[:, 2], label='Earth')
                # Plot the Rogue planet's position
                ax.plot(vctr_position_Rogue[:, 0], vctr_position_Rogue[:, 1], vctr_position_Rogue[:, 2], label='Rogue Planet', color='brown')

                ax.plot(vctr_position_mars[:, 0], vctr_position_mars[:, 1], vctr_position_mars[:, 2], label='Mars', color='red')

                ax.plot(vctr_position_jupiter[:, 0], vctr_position_jupiter[:, 1], vctr_position_jupiter[:, 2], label='Jupiter', color='tan')

                ax.plot(vctr_position_mercury[:, 0], vctr_position_mercury[:, 1], vctr_position_mercury[:, 2], label='mercury', color='orange')

                ax.plot(vctr_position_venus[:, 0], vctr_position_venus[:, 1], vctr_position_venus[:, 2], label='venus', color='gold')

                ax.plot(vctr_position_moon[:, 0], vctr_position_moon[:, 1], vctr_position_moon[:, 2], label='moon', color='gray')


                # Plot the Sun's position
                ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')

                # Add starting points 
                ax.scatter(vctr_position_earth[0, 0], vctr_position_earth[0, 1], vctr_position_earth[0, 2], color='blue', s=50, label='Earth Start')
                ax.scatter(vctr_position_Rogue[0, 0], vctr_position_Rogue[0, 1], vctr_position_Rogue[0, 2], color='red', s=50, label='Rogue Planet Start')
                ax.scatter(vctr_position_moon[0, 0], vctr_position_moon[0, 1], vctr_position_moon[0, 2], color='gray', s=50, label='Moon Start')

                ax.set_xlim([0.88*-1e8, 0.87*-1e8])
                ax.set_ylim([1.245*-1e8, 1.255*-1e8])
                ax.set_zlim([-1e7, 1e7])
                # Customize the plot
                ax.set_xlabel('X Position (km)')
                ax.set_ylabel('Y Position (km)')
                ax.set_zlabel('Z Position (km)')
                ax.set_title('Solar System and the Rogue Planet Positions Over Time in 3D')
                ax.legend()
                ax.grid(True)
                # If there is no file create one
                output_dir = "DATASET_F_photos_SmallAx"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # List the files in the directory
                existing_files = os.listdir(output_dir)

                # List the files in the directory and filter only .png files
                existing_files = [f for f in os.listdir(output_dir) if f.endswith('.png')]

                # Create a new photo name
                plot_number = len(existing_files) + 1
                file_name = f"plot_{plot_number}.png"
                file_path = os.path.join(output_dir, file_name)

                # Save the picture
                plt.savefig(file_path)
                plt.close()

            SmallAx()

            def BigAx():
                fig = plt.figure(figsize=(10, 10))
                ax = fig.add_subplot(111, projection='3d')
                ax.plot(vctr_position_earth[:, 0], vctr_position_earth[:, 1], vctr_position_earth[:, 2], label='Earth')
                # Plot the Rogue planet's position
                ax.plot(vctr_position_Rogue[:, 0], vctr_position_Rogue[:, 1], vctr_position_Rogue[:, 2], label='Rogue Planet', color='brown')

                ax.plot(vctr_position_mars[:, 0], vctr_position_mars[:, 1], vctr_position_mars[:, 2], label='Mars', color='red')

                ax.plot(vctr_position_jupiter[:, 0], vctr_position_jupiter[:, 1], vctr_position_jupiter[:, 2], label='Jupiter', color='tan')

                ax.plot(vctr_position_mercury[:, 0], vctr_position_mercury[:, 1], vctr_position_mercury[:, 2], label='mercury', color='orange')

                ax.plot(vctr_position_venus[:, 0], vctr_position_venus[:, 1], vctr_position_venus[:, 2], label='venus', color='gold')

                ax.plot(vctr_position_moon[:, 0], vctr_position_moon[:, 1], vctr_position_moon[:, 2], label='moon', color='gray')


                # Plot the Sun's position
                ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')

                # Add starting points 
                ax.scatter(vctr_position_earth[0, 0], vctr_position_earth[0, 1], vctr_position_earth[0, 2], color='blue', s=50, label='Earth Start')
                ax.scatter(vctr_position_Rogue[0, 0], vctr_position_Rogue[0, 1], vctr_position_Rogue[0, 2], color='red', s=50, label='Rogue Planet Start')
                ax.scatter(vctr_position_moon[0, 0], vctr_position_moon[0, 1], vctr_position_moon[0, 2], color='gray', s=50, label='Moon Start')


                # Customize the plot
                ax.set_xlabel('X Position (km)')
                ax.set_ylabel('Y Position (km)')
                ax.set_zlabel('Z Position (km)')
                ax.set_title('Solar System and the Rogue Planet Positions Over Time in 3D')
                ax.legend()
                ax.grid(True)
                # If there is no file create one
                output_dir = "DATASET_F_photos_BigAx"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # List the files in the directory
                existing_files = os.listdir(output_dir)

                # List the files in the directory and filter only .png files
                existing_files = [f for f in os.listdir(output_dir) if f.endswith('.png')]

                # Create a new photo name
                plot_number = len(existing_files) + 1
                file_name = f"plot_{plot_number}.png"
                file_path = os.path.join(output_dir, file_name)

                # Save the picture
                plt.savefig(file_path)
                plt.close()

            BigAx()

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
                    line_earth.set_data(vctr_position_earth[:frame, 0], vctr_position_earth[:frame, 1])
                    line_earth.set_3d_properties(vctr_position_earth[:frame, 2])
                    line_rogue.set_data(vctr_position_Rogue[:frame, 0], vctr_position_Rogue[:frame, 1])
                    line_rogue.set_3d_properties(vctr_position_Rogue[:frame, 2])
                    line_jupiter.set_data(vctr_position_jupiter[:frame, 0], vctr_position_jupiter[:frame, 1])
                    line_jupiter.set_3d_properties(vctr_position_jupiter[:frame, 2])
                    line_sun.set_data([0], [0])
                    line_sun.set_3d_properties([0])
                    return line_earth, line_rogue, line_jupiter, line_sun

                total_frames = 15 * 10  # 15 seconds at 10 fps

                # Calculate the step size to ensure the whole video is shown from start to finish
                step_size = len(vctr_position_earth) // total_frames

                # Create the animation with the calculated step size
                ani = FuncAnimation(fig, update, frames=range(0, len(vctr_position_earth), step_size), init_func=init, blit=True)

                # Save the animation as a .mov file using the QuickTime (qt) writer
                ani.save('Dataset_M.mp4', writer='qt', fps=10)
                plt.show()

            AxVid()


            elapsed_time = end_time - start_time
           
            # Mevcut Excel dosyasının varlığını kontrol et ve oku
            file_path = 'DATASET_F.xlsx'

            if os.path.exists(file_path):
                existing_df = pd.read_excel(file_path)
            else:
                existing_df = pd.DataFrame()


            new_data = {
                    'total simulation time(days)':[total_time/86400],
                    'dt(seconds)':[dt],
                    'Angle Alpha': [Alpha_degree],
                    'Sub' : [sub],
                    'Rogue planets speed in Z' : [-10 -V*10],
                    'Earth and Rogue min distance': [min_distance_global],
                    'Rogue and moon min distance': [min_distance_Rogue_moon_global],
                    'Max distance between Earth and moon': [max_distance_Earth_moon_global],
                    'Amount earth has deviated because of Rogue': [np.linalg.norm(vctr_position_earth0[n]-vctr_position_earth[n])],
                    'Roche limit check between Earth and Rogue': [Roche_limit_Rogue_Earth_check],
                    'Roche limit check between Earth and moon': [Roche_limit_Earth_Moon_check],
                    'Roche limit check between Rogue and moon': [Roche_limit_Rogue_Moon_check],
                    
                        }
            """'Roche limit check between Earth and Rogue': [Roche_limit_Rogue_Earth_check],
                    'Roche limit check between Earth and moon': [Roche_limit_Earth_Moon_check],
                'Roche limit check between Rogue and moon': [Roche_limit_Rogue_Moon_check],
                'Roche limit  between Earth and Rogue': [Roche_limit_Rogue_Earth],
                    'Roche limit  between Earth and moon': [Roche_limit_Earth_Moon],
                'Roche limit  between Rogue and moon': [Roche_limit_Rogue_Moon], """
                

            

            new_df = pd.DataFrame(new_data)
            # Mevcut verilerle yeni verileri birleştirin
            combined_df = pd.concat([existing_df, new_df], ignore_index=True)

            # Excel dosyasına yaz
            with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
                combined_df.to_excel(writer, index=False)

    
