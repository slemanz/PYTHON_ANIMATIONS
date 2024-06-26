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
a = 400
n2 = 2
x = a*t**n2

# Create a y array
altitude = 2
# y=np.ones(int(t_end/dt + 1))*altitude
y=np.ones(len(t))*altitude #other way

# speed x 
speed_x = n2*a*t**(n2-1) # using derivate formula



############################### ANIMATION ###############################

frame_amount = int(len(t))

dot = np.zeros(frame_amount)
n = 20

for i in range(0, frame_amount):
    if i == n:
        dot[i] = x[i]
        n = n + 20
    else:
        dot[i] = x[n-20]



def update_plot(num):

    plane_trajectory.set_data(dot[0:num], y[0:num]) 
    plane_1.set_data([x[num] - 40,x[num]+20],[2,2])
    plane_2.set_data([x[num],x[num] -20],[y[num],y[num] + 0.3])
    plane_3.set_data([x[num],x[num] -20],[y[num],y[num] - 0.3])
    plane_4.set_data([x[num]-30,x[num]-40],[y[num],y[num] - 0.15])
    plane_5.set_data([x[num]-30,x[num]-40],[y[num],y[num] + 0.15])

    plane_vertical.set_data([x[num],x[num]], [0, y[num]])

    stopwatch0.set_text(str(round(t[num], 1)) + ' hrs')
    dist_counter0.set_text(str(int(x[num])) + ' km')


    # 2nd plot
    x_dist.set_data(t[0:num], x[0:num])
    horizontal_line.set_data([t[0],t[num]],[x[num],x[num]])
    vertical_line.set_data([t[num],t[num]],[x[0],x[num]])

    # 3rd plot
    speed_line.set_data(t[0:num], speed_x[0:num])

    speed_text3.set_text("dX/dt = " + str(int(speed_x[num])) + " km/h")

    return plane_trajectory, plane_1,plane_2, plane_3, plane_4, plane_5,\
    stopwatch0, dist_counter0, x_dist, horizontal_line, speed_x,\
    speed_text3


fig = plt.figure(figsize=[16,9], dpi=100, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

plane_trajectory,=ax0.plot([],[],'r:o',linewidth=2) # ,= is for remove brackets from our information
plane_vertical,=ax0.plot([],[],'k:o', linewidth=2)

plane_1,= ax0.plot([],[],'k', linewidth=10)  # center of airplane
plane_2,= ax0.plot([],[],'k', linewidth=5)  # first wing
plane_3,= ax0.plot([],[],'k', linewidth=5)  # second wing
plane_4,= ax0.plot([],[],'k', linewidth=3)  # first tail
plane_5,= ax0.plot([],[],'k', linewidth=3)  # second tail



# draw houses
house_1,=ax0.plot([100,100],[0,1.0], 'k', linewidth=7)
house_2,=ax0.plot([300,300],[0,1.0], 'k', linewidth=7)
house_3,=ax0.plot([700,700],[0,0.7], 'k', linewidth=15)
house_4,=ax0.plot([900,900],[0,1.0], 'k', linewidth=10)
house_5,=ax0.plot([1300,1300],[0,1.0], 'k', linewidth=20)

box_object = dict(boxstyle='square', fc=(0.9,0.9,0.9), ec='g', lw=2)
stopwatch0 = ax0.text(1400, 0.75, '', size=14, color='g', bbox=box_object)

box_object2 = dict(boxstyle='square', fc=(0.9,0.9,0.9), ec='r', lw=2)
dist_counter0 = ax0.text(1400, 0.25, '', size=14, color='r', bbox=box_object2)


# subplot properties
plt.xlim(x[0], x[-1])
plt.ylim(0, y[-1]+1)
plt.xticks(np.arange(x[0], x[-1] + 1, x[-1]/4), size=12) # cut in 4 pieces the x
plt.yticks(np.arange(0,y[-1]+2, y[-1]/y[-1]), size=12) # (0, 2+2, 2/2)
plt.xlabel('x-distance', fontsize=12)
plt.ylabel('y-distance', fontsize=12)
plt.title('Airplane', fontsize=16)
plt.grid(True)


# subplot 2

ax2=fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
x_dist,=ax2.plot([],[], '-b', linewidth=3, label='X= '+str(a)+'*t^'+str(n2))
horizontal_line,=ax2.plot([],[],'r:o', linewidth=2, label='distance covered')
vertical_line,=ax2.plot([],[],'g:o', linewidth=2, label='time spent')

plt.xlim(t[0], t[-1])
plt.ylim(x[0], x[-1])
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1]/4), size=12) 
plt.yticks(np.arange(x[0], x[-1] + 1, x[-1]/4), size=12) 
plt.xlabel('time [hrs]', fontsize=12)
plt.ylabel('x-distance [km]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left', fontsize=12)

# subplot 3


ax3=fig.add_subplot(gs[1,1], facecolor=(0.9,0.9,0.9))
speed_line,=ax3.plot([],[], '-b', linewidth=3, label='dX/dt: '+ str(n2*a) +'*t^('+str(n2-1)+')')
vertical_line2,=ax3.plot([],[],'b:o', linewidth=2, label='speed')


speed_text3 = ax3.text(0.20, 965, '', size=14, color='b')

plt.xlim(t[0], t[-1])
plt.ylim(0, speed_x[-1])
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1]/4), size=12) 
plt.yticks(np.arange(0,  speed_x[-1]+1, (speed_x[-1])/4), size=12) 

plt.xlabel('time [hrs]', fontsize=12)
plt.ylabel('speed [km/h]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper right', fontsize=12)



plane_ani = animation.FuncAnimation(fig, update_plot, 
        frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()