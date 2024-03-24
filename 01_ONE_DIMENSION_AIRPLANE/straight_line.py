import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np 

# Set up the duration for your animation
t0 = 0 # time in hours!
t_end = 2
dt = 0.005

# Create array for time
t = np.arange(t0, t_end+dt, dt)

# Create an array for x (km)
x = 800*t

# Create a y array
altitude = 2
# y=np.ones(int(t_end/dt + 1))*altitude
y=np.ones(len(t))*altitude #other way




############################### ANIMATION ###############################

frame_amount = int(len(t))

def update_plot(num):

    plane_trajectory.set_data(x[0:num], y[0:num]) 
    plane_1.set_data([x[num] - 40,x[num]+20],[2,2])
    plane_2.set_data([x[num],x[num] -20],[y[num],y[num] + 0.3])
    plane_3.set_data([x[num],x[num] -20],[y[num],y[num] - 0.3])

    return plane_trajectory, plane_1


fig = plt.figure(figsize=[16,9], dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

plane_trajectory,=ax0.plot([],[],'g',linewidth=2) # ,= is for remove brackets from our information
plane_1,= ax0.plot([],[],'k', linewidth=10)  # center of airplane
plane_2,= ax0.plot([],[],'k', linewidth=5)  # first wing
plane_3,= ax0.plot([],[],'k', linewidth=5)  # second wing



# draw houses
house_1,=ax0.plot([100,100],[0,1.0], 'k', linewidth=7)
house_2,=ax0.plot([300,300],[0,1.0], 'k', linewidth=7)
house_3,=ax0.plot([700,700],[0,0.7], 'k', linewidth=15)
house_4,=ax0.plot([900,900],[0,1.0], 'k', linewidth=10)
house_5,=ax0.plot([1300,1300],[0,1.0], 'k', linewidth=20)



plt.xlim(x[0], x[-1])
plt.ylim(0, y[-1]+1)


plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()