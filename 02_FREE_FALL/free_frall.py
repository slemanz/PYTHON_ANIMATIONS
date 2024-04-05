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
