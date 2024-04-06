import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# time array
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0, t_end+dt, dt)


# gravitational accelerations
g_earth = 9.8 # [m/s^2]


# position y arrays
n = 2
y_i = 100 # [m]
y_earth=y_i + 0.5*g_earth*t**n


# velocity y arrays
y_earth_velocity= n*0.5*g_earth*t**(n-1)


# acceleration y arrays
y_earth_acceleration = (n-1)*g_earth*t**(n-2)


# create circles
def create_circle(r):
    degrees=np.arange(0,361,1)
    radians=degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 5 # [meters]
sphere_x_earth, sphere_y_earth = create_circle(radius)

'''
        ANIMATION
'''

frame_amount = len(t)
width_ratio = 1.2
y_f = - 10  # [m]
dy = 10 # [m]

def update__plot(num):

    return