import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time
t0=0 # [s]
t_end = 60 # [s]
dt = 0.04
t=np.arange(t0,t_end+dt,dt)
