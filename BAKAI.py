# Muzaffer Mahi Can, 18/07/2024, beginning date of the simulation is 16/05


import time
import numpy as np
from numba import njit, prange  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import pandas as pd  
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

start_time = time.perf_counter() #Starts counting time untill code finishes


dt =  720  #Time that acceleration is assumed to be constant, smaller is better

total_time = 86400 * 365.24219 *3 #Total simulation time.

n = int(total_time/dt) -1

#Define position-velocity-acceleraiton vectors for floats
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


#Define the net distance between objects 
net_distance_mars = np.zeros((int(total_time/dt), 3))
net_distance_earth = np.zeros((int(total_time/dt), 3))
net_distance_jupiter = np.zeros((int(total_time / dt), 3))
net_distance_sun = np.zeros(int(total_time / dt))
net_distance_sun[0] = np.linalg.norm(vctr_position_Rogue[0])


#Define the distances of floats to Rogue as norm
norm_distance_earth = np.zeros(int(total_time/dt))
norm_distance_mars = np.zeros(int(total_time/dt))
norm_distance_venus = np.zeros(int(total_time/dt))
norm_distance_mercury = np.zeros(int(total_time/dt))
norm_distance_jupiter = np.zeros(int(total_time/dt))
norm_distance_saturn = np.zeros(int(total_time/dt))
norm_distance_uranus = np.zeros(int(total_time/dt))
norm_distance_neptune = np.zeros(int(total_time/dt))

#Beginning position and velocities 

#vctr_position_Rogue[0] = np.array([-8.403469798266047E+07 ,-1.257970149898590E+08 , 7.300362189300358E+03]) #1 for position of earth 1 day later
vctr_position_Rogue[0] = np.array([-8.192430073178585E+07 ,-1.272173964759768E+08 , 7.450193614929914E+03]) #2 for position of earth 2 days later
#vctr_position_Rogue[0] = np.array([-7.979069907052615E+07 ,-1.286013791239102E+08 , 7.604837871909142E+03]) #3 for position of earth 3 days later
#vctr_position_Rogue[0] = np.array([-7.103668121693499E+07 ,-1.337669136103462E+08 , 8.188007626526058E+03]) #4 for position of earth 7 days later
#vctr_position_Rogue[0] = np.array([-5.496568090604365E+07 ,-1.413345036924672E+08 ,8.525417193897069E+03]) #5 for position of earth 14 days later
#vctr_position_Rogue[0] = np.array([-1.319819903425781E+07 ,-1.513925089860717E+08 , 8.589958537250757E+03]) #6 for position of earth 30 days later
#vctr_position_Rogue[0] = np.array([6.094786707637349E+07 ,-1.393001112076881E+08 , 7.739797480605543E+03]) #7 for position of earth 60 days later
#vctr_position_Rogue[0] = np.array([1.214435411459364E+08 ,-9.054815377135754E+07 , 4.820373744789511E+03]) #8 for position of earth 90 days later
#vctr_position_Rogue[0] = np.array([8.742188518307206E+07 , 1.193449153176520E+08 ,-7.527354944825172E+03]) #9 for position of earth 180 days later

#vctr_position_Rogue[0] = np.array([3.659158469107834E+07 ,-5.245042976724952E+07 ,-7.642607617650028E+06]) #10 for position of Mercury 1 day later
#vctr_position_Rogue[0] = np.array([4.930589823369529E+07 ,-3.345822779222985E+07 ,-7.256741475936791E+06]) #11 for position of Mercury 7 days later
#vctr_position_Rogue[0] = np.array([-1.662230708274036E+06 , 4.606515971097183E+07 , 3.916959025492180E+06]) #12 for position of Mercury 30 days later

#vctr_position_Rogue[0] = np.array([7.748462159990992E+07 , 7.540528477895698E+07 ,-3.435339931190711E+06]) #13 for position of Venus 1 day later
#vctr_position_Rogue[0] = np.array([6.373760256672546E+07 ,8.721674238353182E+07 ,-2.479911204471711E+06]) #14 for position of Venus 7 days later
#vctr_position_Rogue[0] = np.array([-4.689237482169829E+06 , 1.075262204437541E+08 ,1.747299759375595E+06]) #15 for position of Venus 30 days later

#vctr_position_Rogue[0] = np.array([1.960996908913333E+08 ,-6.520720178278370E+07 ,-6.176599457135249E+06]) #16for position of Mars 1 day later
#vctr_position_Rogue[0] = np.array([2.001432678918751E+08 ,-5.209303687728728E+07 ,-6.000943334853865E+06]) #17 for position of Mars 7 days later
#vctr_position_Rogue[0] = np.array([2.081789308857712E+08 ,1.918008752198097E+06 ,-5.066114996689608E+06]) #18 for position of Mars 30 days later

#vctr_position_Rogue[0] = np.array([3.995775467812629E+08 , 6.349329425509669E+08 ,-1.157731095597476E+07]) #19 for position of Jupiter 1 day later
#vctr_position_Rogue[0] = np.array([3.937443706704275E+08 , 6.388362922929692E+08 ,-1.146302096492144E+07]) #20 for position of Jupiter 7 days later
#vctr_position_Rogue[0] = np.array([3.700848689190053E+08 , 6.539074853354003E+08 ,-1.099627952234486E+07]) #21 for position of Jupiter 30 days later

#vctr_position_Rogue[0] = np.array([1.378914041910695E+09 ,-4.487937158335014E+08 ,-4.707526734372568E+07]) #22 for position of Saturn 1 day later
#vctr_position_Rogue[0] = np.array([1.380173818851141E+09 ,-4.440354070558689E+08 ,-4.720802165455639E+07]) #23 for position of Saturn 7 days later
#vctr_position_Rogue[0] = np.array([1.385052925169666E+09 ,-4.249496814107042E+08 ,-4.773448663103661E+07]) #24 for position of Saturn 30 days later

#vctr_position_Rogue[0] = np.array([1.771448157519348E+09 ,2.334836774807115E+09, -1.429616907952344E+07]) #25 for position of Uranus 1 day later
#vctr_position_Rogue[0] = np.array([1.768602827014709E+09 , 2.336809240868641E+09 ,-1.425196420368326E+07]) #26 for position of Uranus 7 days later
#vctr_position_Rogue[0] = np.array([1.757195992384523E+09 , 2.344665358282034E+09 ,-1.407506836855304E+07]) #27 for position of Uranus 30 days later

vctr_velocity_Rogue[0] = np.array([1.176261267381250E+01,-3.023110865122838E+01,-4.772431731046794])

vctr_position_earth[0] = np.array([-8.612126415163520E+07 ,-1.243405742161587E+08 , 7.159140121236444E+03])
vctr_velocity_earth[0] = np.array([2.400973596546069E+01 ,-1.706428457849702E+01 , 1.571000011289847E-03])

vctr_position_earth0[0] = np.array([-8.612126415163520E+07 ,-1.243405742161587E+08 , 7.159140121236444E+03])
vctr_velocity_earth0[0] = np.array([2.400973596546069E+01 ,-1.706428457849702E+01 , 1.571000011289847E-03])

vctr_position_moon[0] = np.array([-8.755507860116081E+07,-1.247124832815350E+08 ,6.257550822596997E+04])
vctr_velocity_moon[0] = np.array([2.352284152220006E+01 ,-1.790602303115681E+01 ,-6.028641210510699E-02])

vctr_position_venus[0] = np.array([7.957344843384959E+07 , 7.322053343986090E+07 ,-3.585871528166533E+06])
vctr_velocity_venus[0] = np.array([-2.381909462246481E+01 , 2.562129936835433E+01 , 1.726254783991651E+00])

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
M_SUN= float(1989000000000000000000000000000)
M_JUPITER = float(1898130000000000000000000000)
M_earth = float(5972200000000000000000000)
M_MARS = float(639000000000000000000000)
M_VENUS = float(4800000000000000000000000)
M_mercury = float(328500000000000000000000)
M_SATURN = float(5683 * 10**23)
M_URANUS = float(8681 * 10**22)
M_NEPTUNE = float(10**26)
M_Rogue = float(10 * M_JUPITER)
M_Moon =    7.34767309 * 10**22

net_distance_earth[0] = np.array(vctr_position_earth[0]- vctr_position_Rogue[0])


Collision = False
#Calculate positions of Rogue and distances from floats for Total Time
@njit
def compute_position(total_time, dt, G, M_SUN, M_earth, M_VENUS, M_MARS, M_mercury, M_JUPITER, M_SATURN, M_NEPTUNE, M_URANUS, M_Rogue, 
                     vctr_position_Rogue, vctr_velocity_Rogue, vctr_acceleration_Rogue, 
                     vctr_position_earth, vctr_velocity_earth, vctr_acceleration_earth,
                     vctr_position_venus, vctr_velocity_venus, vctr_acceleration_venus,
                     vctr_position_mars, vctr_velocity_mars, vctr_acceleration_mars,
                     vctr_position_mercury, vctr_velocity_mercury, vctr_acceleration_mercury,
                     vctr_position_jupiter, vctr_velocity_jupiter, vctr_acceleration_jupiter,
                     vctr_position_saturn, vctr_velocity_saturn, vctr_acceleration_saturn,
                     vctr_position_neptune, vctr_velocity_neptune, vctr_acceleration_neptune,
                     vctr_position_uranus, vctr_velocity_uranus, vctr_acceleration_uranus,
                     vctr_position_earth0, vctr_velocity_earth0, vctr_acceleration_earth0): 
    
    for n in range(1, int(total_time/dt )):

        vctr_acceleration_Rogue[n] = (- G * M_SUN* vctr_position_Rogue[n-1]/np.linalg.norm(vctr_position_Rogue[n-1])**3
        - G * M_earth * (vctr_position_Rogue[n-1]-vctr_position_earth[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_earth[n-1]**3)
        - G * M_VENUS * (vctr_position_Rogue[n-1]-vctr_position_venus[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_venus[n-1])**3
        - G * M_MARS * (vctr_position_Rogue[n-1]-vctr_position_mars[n-1])/(np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_mars[n-1])**3)
        - G * M_mercury * (vctr_position_Rogue[n-1]-vctr_position_mercury[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_mercury[n-1])**3
        - G * M_JUPITER* (vctr_position_Rogue[n-1]-vctr_position_jupiter[n-1])/np.linalg.norm(vctr_position_Rogue[n-1]-vctr_position_jupiter[n-1])**3
    
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
        
        - G * M_Rogue* (vctr_position_earth[n-1] - vctr_position_Rogue[n-1])/np.linalg.norm(vctr_position_earth[n-1] - vctr_position_Rogue[n-1])**3
        )

        vctr_velocity_earth[n] = vctr_velocity_earth[n-1] + vctr_acceleration_earth[n-1]*dt
        vctr_position_earth[n] = vctr_position_earth[n-1] + vctr_velocity_earth[n-1]*dt + 0.5*dt**2*vctr_acceleration_earth[n-1]

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


        vctr_acceleration_saturn[n] = (-G * M_SUN * vctr_position_saturn[n-1]/np.linalg.norm(vctr_position_saturn[n-1])**3
        - G * M_Rogue* (vctr_position_saturn[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_saturn[n-1] - vctr_position_Rogue[n-1])**3))
        vctr_velocity_saturn[n] = vctr_velocity_saturn[n-1] + vctr_acceleration_saturn[n-1]*dt
        vctr_position_saturn[n] = vctr_position_saturn[n-1] + vctr_velocity_saturn[n-1]*dt + 0.5*dt**2*vctr_acceleration_saturn[n-1]

        vctr_acceleration_uranus[n] = (-G * M_SUN * vctr_position_uranus[n-1]/np.linalg.norm(vctr_position_uranus[n-1])**3
        - G * M_Rogue* (vctr_position_uranus[n-1] - vctr_position_Rogue[n-1])/(np.linalg.norm(vctr_position_uranus[n-1] - vctr_position_Rogue[n-1])**3))
        vctr_velocity_uranus[n] = vctr_velocity_uranus[n-1] + vctr_acceleration_uranus[n-1]*dt
        vctr_position_uranus[n] = vctr_position_uranus[n-1] + vctr_velocity_uranus[n-1]*dt + 0.5*dt**2*vctr_acceleration_uranus[n-1]

        if np.linalg.norm(vctr_position_earth[n]-vctr_position_Rogue[n]) < 20000:
            print("Rogue and Earth collided")
            Collision = True
            break
            
       
                
        if np.linalg.norm(vctr_position_venus[n]-vctr_position_Rogue[n]) < 6000:
            print("Venus and Rogue collided")

        if np.linalg.norm(vctr_position_mercury[n]-vctr_position_Rogue[n]) < 2500:
            print("Mercury and Rogue collided")
        
        if np.linalg.norm(vctr_position_mars[n]-vctr_position_Rogue[n]) < 3300:
            print("Mars and Rogue collided")

        if np.linalg.norm(vctr_position_jupiter[n]-vctr_position_Rogue[n]) < 70000:
            print("Jupiter and Rogue collided")

        if np.linalg.norm(vctr_position_saturn[n]-vctr_position_Rogue[n]) < 60000:
            print("Saturn and Rogue collided")

        if np.linalg.norm(vctr_position_uranus[n]-vctr_position_Rogue[n]) < 25000:
            print("Uranus and Rogue collided")
    

compute_position(total_time, dt, G, M_SUN, M_earth, M_VENUS, M_MARS, M_mercury, M_JUPITER, M_SATURN, M_NEPTUNE, M_URANUS, M_Rogue, 
                     vctr_position_Rogue, vctr_velocity_Rogue, vctr_acceleration_Rogue, 
                     vctr_position_earth, vctr_velocity_earth, vctr_acceleration_earth,
                     vctr_position_venus, vctr_velocity_venus, vctr_acceleration_venus,
                     vctr_position_mars, vctr_velocity_mars, vctr_acceleration_mars,
                     vctr_position_mercury, vctr_velocity_mercury, vctr_acceleration_mercury,
                     vctr_position_jupiter, vctr_velocity_jupiter, vctr_acceleration_jupiter,
                     vctr_position_saturn, vctr_velocity_saturn, vctr_acceleration_saturn,
                     vctr_position_neptune, vctr_velocity_neptune, vctr_acceleration_neptune,
                     vctr_position_uranus, vctr_velocity_uranus, vctr_acceleration_uranus,
                     vctr_position_earth0, vctr_velocity_earth0, vctr_acceleration_earth0)

#End time counter
end_time = time.perf_counter()
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(vctr_position_earth[:, 0], vctr_position_earth[:, 1], vctr_position_earth[:, 2], label='Earth')

# Plot the Rogue planet's position
ax.plot(vctr_position_Rogue[:, 0], vctr_position_Rogue[:, 1], vctr_position_Rogue[:, 2], label='Rogue Planet', color='brown')

ax.plot(vctr_position_mars[:, 0], vctr_position_mars[:, 1], vctr_position_mars[:, 2], label='Mars', color='red')

ax.plot(vctr_position_jupiter[:, 0], vctr_position_jupiter[:, 1], vctr_position_jupiter[:, 2], label='Jupiter', color='tan')

ax.plot(vctr_position_uranus[:, 0], vctr_position_uranus[:, 1], vctr_position_uranus[:, 2], label='uranus', color='green')

ax.plot(vctr_position_mercury[:, 0], vctr_position_mercury[:, 1], vctr_position_mercury[:, 2], label='mercury', color='orange')

ax.plot(vctr_position_venus[:, 0], vctr_position_venus[:, 1], vctr_position_venus[:, 2], label='venus', color='gold')

ax.plot(vctr_position_saturn[:, 0], vctr_position_saturn[:, 1], vctr_position_saturn[:, 2], label='saturn', color='blue')

# Plot the Sun's position
ax.scatter(0, 0, 0, color='yellow', s=100, label='Sun')

ax.set_xlim([-1e9, 1e9])
ax.set_ylim([-1e9, 1e9])
ax.set_zlim([-1e9, 1e9])
# Customize the plot
ax.set_xlabel('X Position (km)')
ax.set_ylabel('Y Position (km)')
ax.set_zlabel('Z Position (km)')
ax.set_title('Solar System and the Rogue Planet Positions Over Time in 3D')
ax.legend()
ax.grid(True)

# If there is no file create one
output_dir = "simulation_photos"
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

print(f"Picture is saved to '{file_path}' ")

elapsed_time = end_time - start_time
print(f"Elapsed time: (s) {elapsed_time}\n")
print(f"Earth's first position: {vctr_position_earth[0]}\n")
print(f"Earths's last position WİTHOUT Rogue{vctr_position_earth0[n]}")
print(f"Earth's last position: {vctr_position_earth[n]}")
print(f"Earth's last velocity: {vctr_velocity_earth[n]}\n")
print(f"Earth's last position difference between rogue and no rogue:{np.linalg.norm(vctr_position_earth0[n]-vctr_position_earth[n])} km")
print(f"Venus last position: {vctr_position_venus[n]}") 
print(f"Mars first position: {vctr_position_mars[0]}")
print(f"Mars last position: {vctr_position_mars[n]}\n")
print(f"Jupiter's first position: {vctr_position_jupiter[0]}")
print(f"Jupiter's last position{vctr_position_jupiter[n]}\n")
print(f"Np.linalg.norm velocity of rogue at beginning: {np.linalg.norm(vctr_velocity_Rogue[0])}")

# Mevcut Excel dosyasının varlığını kontrol et ve oku
file_path = 'simulation_results.xlsx'

if os.path.exists(file_path):
    existing_df = pd.read_excel(file_path)
else:
    existing_df = pd.DataFrame()

# Yeni verileri ekleyin
if Collision == True:
    new_data = {
        'Calculation number': [plot_number],
        'Earth position difference between Rogue and no Rogue, km': [np.linalg.norm(vctr_position_earth0[n]-vctr_position_earth[n])],
        'Earth_last_position': [vctr_position_earth[n].tolist()],
        'Total_time_days': [total_time / 86400],
        'Collision_check Earth-Rogue': ["True"]
    
        }
else:
        new_data = {
        'Calculation number': [plot_number],
        'Earth position difference between Rogue and no Rogue, km': [np.linalg.norm(vctr_position_earth0[n]-vctr_position_earth[n])],
        'Earth_last_position': [vctr_position_earth[n].tolist()],
        'Total_time_days': [total_time / 86400],
        'Collision_check Earth-Rogue': ["False"]
        }
new_df = pd.DataFrame(new_data)

# Mevcut verilerle yeni verileri birleştirin
combined_df = pd.concat([existing_df, new_df], ignore_index=True)

# Excel dosyasına yaz
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    combined_df.to_excel(writer, index=False)

print(f"Data successfully written to Excel file named {file_path}")
print(Collision)
# Show the plot
plt.show()
print(np.linalg.norm(vctr_position_earth[1000]-vctr_position_Rogue[1000]))
