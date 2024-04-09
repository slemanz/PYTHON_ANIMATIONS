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
g_earth = -9.8 # [m/s^2]
g_mars = -3.71
g_moon = -1.625

# position y arrays
n = 2
y_i = 100 # [m]
y_earth = y_i + 0.5*g_earth*t**n
y_mars = y_i + 0.5*g_mars*t**n
y_moon = y_i + 0.5*g_moon*t**n



# velocity y arrays
y_earth_velocity= n*0.5*g_earth*t**(n-1)
y_mars_velocity= n*0.5*g_mars*t**(n-1)
y_moon= n*0.5*g_moon*t**(n-1)


# acceleration y arrays
y_earth_acceleration = (n-1)*g_earth*t**(n-2)
y_mars_acceleration = (n-1)*g_mars*t**(n-2)
y_moon_acceleration = (n-1)*g_moon*t**(n-2)



# create circles
def create_circle(r):
    degrees=np.arange(0,361,1)
    radians=degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 5 # [meters]
sphere_x_earth, sphere_y_earth = create_circle(radius)
sphere_x_mars, sphere_y_mars = create_circle(radius)
sphere_x_moon, sphere_y_moon = create_circle(radius)

'''
        ANIMATION
'''

frame_amount = len(t)
width_ratio = 1.2
y_f = -10  # [m]
dy = 10 # [m]

def update_plot(num):
    if(y_earth[num] >= radius):
        sphere_earth.set_data(sphere_x_earth, sphere_y_earth+y_earth[num])
        alt_E.set_data(t[0:num], y_earth[0:num])
        vel_E.set_data(t[0:num], y_earth_velocity[0:num])
        acc_E.set_data(t[0:num], y_earth_acceleration[0:num])

    if(y_mars[num] >= radius):
        sphere_mars.set_data(sphere_x_mars, sphere_y_mars+y_mars[num])
        alt_M.set_data(t[0:num], y_mars[0:num])
        vel_M.set_data(t[0:num], y_mars_velocity[0:num])
        acc_M.set_data(t[0:num], y_mars_acceleration[0:num])

    return sphere_earth, alt_E, vel_E, acc_E, alt_M


# figure properties
fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)


# create object for earth
ax0 = fig.add_subplot(gs[:,0], facecolor=(0.9,0.9,0.9))
sphere_earth,=ax0.plot([],[],'k',linewidth=3)
land_Earth=ax0.plot([-radius*width_ratio, radius*width_ratio], [-5,-5],'g', linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.xticks(np.arange(-radius, radius+1, radius))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude [m]')
plt.title('Earth')


# create object for mars
ax1 = fig.add_subplot(gs[:,1], facecolor=(0.9,0.9,0.9))
sphere_mars,=ax1.plot([],[],'k', linewidth=3)
land_Mars=ax1.plot([-radius*width_ratio, radius*width_ratio], [-5,-5],'orangered', linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude [m]')
plt.title('Mars')


# create obejct for moon
ax2 = fig.add_subplot(gs[:,2], facecolor=(0.9,0.9,0.9))
#sphere_mars,=ax2.plot([],[],'k', linewidth=3)
land_Moon=ax2.plot([-radius*width_ratio, radius*width_ratio], [-5,-5],'gray', linewidth=38)
plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f, y_i+dy)
plt.yticks(np.arange(y_f, y_i+2*dy, dy))
plt.ylabel('altitude [m]')
plt.title('Moon')

# create position function
ax3=fig.add_subplot(gs[0,3], facecolor=(0.9,0.9,0.9))
alt_E,=ax3.plot([],[],'g', label='Alt_Earth = '+str(y_i)+'('+str(round(g_earth/2,1))+')t^'+str(n)+' [m]', linewidth=3)
alt_M,=ax3.plot([],[],'orangered', label='Alt_Mars = '+str(y_i)+'('+str(round(g_mars/2,1))+')t^'+str(n)+' [m]', linewidth=3)
plt.xlim(0, t_end)
plt.ylim(0, y_i)
plt.legend(loc=(0.6,0.7), fontsize='x-small')


# Create velocity function
ax4=fig.add_subplot(gs[1,3], facecolor=(0.9,0.9,0.9))
vel_E,=ax4.plot([],[],'g', linewidth=3, label='Vel_Earth = '+str(g_earth)+'t [m/s]')
vel_M,=ax4.plot([],[],'orangered', linewidth=3, label='Vel_Mars = '+str(g_mars)+'t [m/s]')
plt.xlim(0,t_end)
plt.ylim(y_earth_velocity[-1], 0)
plt.legend(loc='lower left', fontsize='x-small')

# create acceleration function

ax5=fig.add_subplot(gs[2,3], facecolor=(0.9,0.9,0.9))
acc_E,=ax5.plot([],[],'g',linewidth=3,label='Acc_Earth = '+str(g_earth)+'[(m/s)s = m/s^2]')
acc_M,=ax5.plot([],[],'orangered',linewidth=3,label='Acc_Mars = '+str(g_mars)+'[(m/s)s = m/s^2]')
plt.xlim(0,t_end)
plt.ylim(g_earth-1,0)
plt.legend(loc=(0.02,0.35), fontsize='x-small')


free_fall=animation.FuncAnimation(fig, update_plot, frame_amount, interval=20, 
                                    repeat=True, blit=True)

plt.show()