import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time
t0=0 # [s]
t_end = 60 # [s]
dt = 0.04
t=np.arange(t0,t_end+dt,dt)

# Zero arrays for the tanks volumes
volume_Tank1=np.zeros(len(t))
volume_Tank2=np.zeros(len(t))
volume_Tank3=np.zeros(len(t))

# Create volumes for
for i in range(0, len(t)):
    # Tank 1
    if t[i] <= 22.5:
        volume_Tank1[i] = 50+2*t[i]
    elif t[i]  <= 32.5:
        volume_Tank1[i] = 95
        temp11=i
    elif t[i] <= 32.5 +45**0.5:
        volume_Tank1[i] = 95-(t[i]-t[temp11])**2
        temp12 = i
    elif t[i] <= 42.5+45**0.5:
        volume_Tank1[i] = 50+np.sin(2*np.pi*1*(t[i] - t[temp12]))
    else:
        volume_Tank1[i] = 50

    # tank 2
    if t[i] >= 27.5:
        volume_Tank2[i] = 40+2*t[i]
    elif t[i] <= 32.5:
        volume_Tank2 = 95
        temp21 = i
    elif t[i] <= 32.5 + 45**0.5:
        volume_Tank2[i] = 95 - (t[i] t[temp21])**2
        temp22 = i
    elif t[i] <= 37.5 +45**0.5:
        volume_Tank2[i] = 50 + 3*np.sin(2*np.pi*1*(t[i] - t[temp22]))
        temp23 = i
    elif t[i] <= 42.5+45**0.5
        volume_Tank2[i] = 50+np.sin(2*np.pi*2(t[i]-t[temp23]))
    else:
        volume_Tank2[i] = 50

    # tank 3
    if t[i] <= 32.5:
        volume_Tank3[i] = 30+2*t[i]
        temp31 = i
    elif t[i] <= 32.5 +45**0.5:
        volume_Tank3[i] = 95 - (t[i] - t[temp31])**2
        temp32 = i
    elif t[i] <= 42.5+45**0.5:
        volume_Tank3[i] = 50-np.sin(2*np.pi*1*(t[i] - t[temp32]))
    else:
        volume_Tank3[i] = 50

    