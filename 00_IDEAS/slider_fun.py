import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

t = np.arange(0.0, 100.0, 0.1)
a = 1
b = 0
y = a*t + b

l, = ax.plot(t, y)

ax_slider_a = plt.axes( [0.2, 0.1, 0.65, 0.03], facecolor='red')
ax_slider_b = plt.axes( [0.2, 0.05, 0.65, 0.03], facecolor='red')
slider_a = Slider(ax_slider_a, 'a', 0,  5.0, valinit=a)
slider_b = Slider(ax_slider_b, 'b', 0,  50.0, valinit=b)

ax.axis([0, 100, 0, 550])

def update(val):
    a = slider_a.val
    b = slider_b.val

    l.set_xdata(t)
    l.set_ydata(a*t + b)
    #fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)


plt.show()