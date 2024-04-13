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

'''
    ANIMATION
'''

frame_amount=len(t)

def update_plot(num):

    return



# set up the figure
fig=plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# subplot 0
ax0=fig.add_subplot(gs[0,0], facecolor=(0.9,0.9,0.9))
x_blue,=ax0.plot([],[],'-b', linewidth=3, label='X_blue = '+str(A1)+'sin(2pi*'+str(f1)+'*t)')
x_red,=ax0.plot([],[],'-r', linewidth=3, label='X_red = '+str(A2)+'sin(2pi*'+str(f2)+'*t)')

plt.xlim(t0,t_end)
plt.ylim(-8,8)
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('X [m]')
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,0)

plt.show()