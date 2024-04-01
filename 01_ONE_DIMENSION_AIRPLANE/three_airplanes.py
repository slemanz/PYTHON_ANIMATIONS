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


# AIRPLANE 1

# Create an array for x (km)
a1 = 800
n1 = 1
x1 = a1*t**n1

# Create a y array
altitude1 = 2
# y=np.ones(int(t_end/dt + 1))*altitude
y1=np.ones(len(t))*altitude1 #other way

# speed x 
speed_x1 = n1*a1*t**(n1-1) # using derivate formula



############################### ANIMATION ###############################

frame_amount = int(len(t))

dot1 = np.zeros(frame_amount)
n = 20

for i in range(0, frame_amount):
    if i == n:
        dot1[i] = x1[i]
        n = n + 20
    else:
        dot1[i] = x1[n-20]



def update_plot(num):

    plane_trajectory1.set_data(dot1[0:num], y1[0:num]) 
    plane1_1.set_data([x1[num] - 40,x1[num]+20],[2,2])
    plane1_2.set_data([x1[num],x1[num] -20],[y1[num],y1[num] + 0.3])
    plane1_3.set_data([x1[num],x1[num] -20],[y1[num],y1[num] - 0.3])
    plane1_4.set_data([x1[num]-30,x1[num]-40],[y1[num],y1[num] - 0.15])
    plane1_5.set_data([x1[num]-30,x1[num]-40],[y1[num],y1[num] + 0.15])




    # 2nd plot
    x_dist1.set_data(t[0:num], x1[0:num])

    # 3rd plot
    speed_line1.set_data(t[0:num], speed_x1[0:num])


    return plane_trajectory1, plane1_1,plane1_2, plane1_3, plane1_4, plane1_5,\
    x_dist1, speed_line1


fig = plt.figure(figsize=[16,9], dpi=100, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

plane_trajectory1,=ax0.plot([],[],'r:o',linewidth=2) # ,= is for remove brackets from our information

plane1_1,= ax0.plot([],[],'k', linewidth=10)  # center of airplane
plane1_2,= ax0.plot([],[],'k', linewidth=5)  # first wing
plane1_3,= ax0.plot([],[],'k', linewidth=5)  # second wing
plane1_4,= ax0.plot([],[],'k', linewidth=3)  # first tail
plane1_5,= ax0.plot([],[],'k', linewidth=3)  # second tail





# subplot properties
plt.xlim(x1[0], x1[-1])
plt.ylim(0, y1[-1]+1)
plt.xticks(np.arange(x1[0], x1[-1] + 1, x1[-1]/4), size=12) # cut in 4 pieces the x
plt.yticks(np.arange(0,y1[-1]+2, y1[-1]/y1[-1]), size=12) # (0, 2+2, 2/2)
plt.xlabel('x-distance', fontsize=12)
plt.ylabel('y-distance', fontsize=12)
plt.title('Airplane', fontsize=16)
plt.grid(True)


# subplot 2

ax2=fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist1,=ax2.plot([],[], '-b', linewidth=3, label='position airplane 1')

plt.xlim(t[0], t[-1])
plt.ylim(x1[0], x1[-1])
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1]/4), size=12) 
plt.yticks(np.arange(x1[0], x1[-1] + 1, x1[-1]/4), size=12) 
plt.xlabel('time [hrs]', fontsize=12)
plt.ylabel('x-distance [km]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left', fontsize=12)

# subplot 3

ax3=fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed_line1,=ax3.plot([],[], '-b', linewidth=3, label='speed airplane 1')

plt.xlim(t[0], t[-1])
plt.ylim(0, speed_x1[-1]*2)
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1]/4), size=12) 
plt.yticks(np.arange(0,  speed_x1[-1]*2+1, (speed_x1[-1]*2)/4), size=12) 

plt.xlabel('time [hrs]', fontsize=12)
plt.ylabel('speed [km/h]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper right', fontsize=12)



plane_ani = animation.FuncAnimation(fig, update_plot, 
        frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()