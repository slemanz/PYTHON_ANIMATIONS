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
y_earth = y_i + 0.5*g_earth*t**n


# velocity y arrays
y_earth_velocity= n*0.5*g_earth*t**(n-1)


# acceleration y arrays
y_earth_acceleration = (n-1)*g_earth*t**(n-2)


# create circles
def create_circle(r):
    degrees=np.arange(0,361,1)
    radians=degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 5 # [meters]
sphere_x_earth, sphere_y_earth = create_circle(radius)

'''
        ANIMATION
'''

frame_amount = len(t)
width_ratio = 1.2
y_f = -10  # [m]
dy = 10 # [m]

def update__plot(num):

    return


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




plt.show()