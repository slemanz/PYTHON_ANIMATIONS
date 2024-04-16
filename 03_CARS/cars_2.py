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
f1=(1/3) # [hz]
A1 = 20   # [m]
train_blue = A1*np.sin(2*np.pi*f1*t)


# red train
f2 = (1/12)  # [hz]
A2 = 5 # [m]
train_red=A2*np.cos(2*np.pi*f2*t)

# Cars
y_i=13
y_ia = np.ones(len(t))*y_i
car_green=y_i-2*(t-2)**2
car_purple=y_i-2*(t-6)

'''
    ANIMATION
'''

frame_amount=len(t)

def update_plot(num):
    # subplot 0
    x_blue.set_data(t[0:num], train_blue[0:num])
    x_red.set_data(t[0:num], train_red[0:num])

    # subplot 1 & 2
    block_blue.set_data([train_blue[num]-0.25, train_blue[num]+0.25], [3.5,3.5])
    block_red.set_data([train_red[num]-0.25, train_red[num]+0.25], [1.5,1.5])
    
    if t[num] >= 2:
        block_green.set_data([3.5,3.5], [car_green[num]-0.5, car_green[num]+0.5])
        Y_green.set_data(t[int(2/dt):num], car_green[int(2/dt):num])
    else:
        block_green.set_data([3.5,3.5], [y_i-0.5, y_i+0.5])
        Y_green2.set_data(t[0:num], y_ia[0:num])

    if t[num] >= 6:
        block_purple.set_data([-3.5,-3.5], [car_purple[num]-0.5, car_purple[num]+0.5])
        Y_purple.set_data(t[int(6/dt):num], car_purple[int(6/dt):num])
    else:
        block_purple.set_data([-3.5,-3.5], [y_i-0.5, y_i+0.5])
        Y_purple2.set_data(t[0:num], y_ia[0:num])

    return x_blue, x_red, block_blue, block_red, block_green, Y_green, block_purple, Y_purple, Y_purple2, Y_green2



# set up the figure
fig=plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# subplot 0
ax0=fig.add_subplot(gs[0,0], facecolor=(0.9,0.9,0.9))
x_blue,=ax0.plot([],[],'-b', linewidth=3, label='X_blue = '+str(A1)+'sin(2π*'+str(f1)+'*t)')
x_red,=ax0.plot([],[],'-r', linewidth=3, label='X_red = '+str(A2)+'cos(2π*'+str(f2)+'*t)')

plt.xlim(t0,t_end)
plt.ylim(-21,21)
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('X [m]')
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5,0)
plt.legend(bbox_to_anchor=(1, 1.2), fontsize='medium')


# subplot 1
ax1=fig.add_subplot(gs[1,0], facecolor=(0.9,0.9,0.9))
Y_purple,=ax1.plot([],[],'m',linewidth=5)
Y_purple2,=ax1.plot([],[],'m',linewidth=5, alpha=1)
Y_green,=ax1.plot([],[],'g',linewidth=3)
Y_green2,=ax1.plot([],[],'g',linewidth=3)

plt.xlim(t0,t_end)
plt.ylim(-2, y_i+1)
plt.grid(True)
plt.xlabel('time [s]')
plt.ylabel('Y [m]')
ax1.spines['bottom'].set_position(('data',0))
#ax1.spines['left'].set_position(('data',0))
ax1.xaxis.set_label_coords(0.5,0)


# subplot 2
ax2=fig.add_subplot(gs[:,1], facecolor=(0.9,0.9,0.9))
block_blue,=ax2.plot([],[], '-b', linewidth=28)
block_red,=ax2.plot([],[], '-r', linewidth=28)
block_green,=ax2.plot([],[], '-g', linewidth=18)
block_purple,=ax2.plot([],[], 'purple', linewidth=18)

# create danger zone 1
danger_zone1_1,=ax2.plot([3,4], [1,1], '-k', linewidth=3)
danger_zone1_2,=ax2.plot([3,4], [2,2], '-k', linewidth=3) 
danger_zone1_3,=ax2.plot([3,3], [1,2], '-k', linewidth=3) 
danger_zone1_4,=ax2.plot([4,4], [1,2], '-k', linewidth=3) 


# create danger zone 2
danger_zone2_1,=ax2.plot([3,4], [3,3], '-k', linewidth=3)
danger_zone2_2,=ax2.plot([3,4], [4,4], '-k', linewidth=3) 
danger_zone2_3,=ax2.plot([3,3], [3,4], '-k', linewidth=3) 
danger_zone2_4,=ax2.plot([4,4], [3,4], '-k', linewidth=3) 


# create danger zone 3
danger_zone3_1,=ax2.plot([-3,-4], [1,1], '-k', linewidth=3)
danger_zone3_2,=ax2.plot([-3,-4], [2,2], '-k', linewidth=3) 
danger_zone3_3,=ax2.plot([-3,-3], [1,2], '-k', linewidth=3) 
danger_zone3_4,=ax2.plot([-4,-4], [1,2], '-k', linewidth=3) 


# create danger zone 4
danger_zone4_1,=ax2.plot([-3,-4], [3,3], '-k', linewidth=3)
danger_zone4_2,=ax2.plot([-3,-4], [4,4], '-k', linewidth=3) 
danger_zone4_3,=ax2.plot([-3,-3], [3,4], '-k', linewidth=3) 
danger_zone4_4,=ax2.plot([-4,-4], [3,4], '-k', linewidth=3) 


bbox_green=dict(boxstyle='square', fc=(0.9,0.9,0.9), ec='g', lw=1)
bbox_purple=dict(boxstyle='square', fc=(0.9,0.9,0.9), ec='purple', lw=1)
ax2.text(0.3, y_i+1.5, 'car_green='+str(int(y_i))+'-2(t-2)^2', size=10, color='g', bbox=bbox_green)
ax2.text(-7.8, y_i+1.5, 'car_purple='+str(int(y_i))+'-2(t-6)', size=10, color='purple', bbox=bbox_purple)


plt.xlim(-max(A1,A2)-1, max(A1,A2)+1)
plt.ylim(-2, y_i+1)
plt.grid(True)
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position(('data',0))
plt.xticks(np.concatenate([np.arange(-21,0,2), np.arange(1,20+2,2)]), size=10)
plt.yticks(np.concatenate([np.arange(-2,0,1), np.arange(1,y_i+2,1)]), size=10)

cars=animation.FuncAnimation(fig, update_plot, frame_amount, interval=10, 
                                    repeat=True, blit=True)

plt.show()