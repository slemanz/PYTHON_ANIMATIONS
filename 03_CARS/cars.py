import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Create the time array
t0 = 0
t_end=16
dt = 0.02
t=np.arange(t0,t_end+dt,dt)

'''
    Create arrays for motion
'''
# blue train
f1=0.125 # [hz]
A1 = 7   # [m]
train_blue = A1*np.sin(2*np.pi*f1*t)


# red train
f2 = 0.125  # [hz]
A2 = 7 # [m]
train_red=A2*np.cos(2*np.pi*f2*t)

# Cars
y_i=13
car_green=y_i-2*(t-2)**2
car_purple=y_i-2*(t-6)