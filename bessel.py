import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import gamma, factorial

x = np.linspace(0, 15, 1000)


besselFuncs = []
n = 5


for i in range(n):
    y = np.zeros_like(x)
    for j in range(150):
        h = np.power(x/2.0, 2*j + i) * (-1)**j
        h /= factorial(j)
        h /= gamma(j + i + 1)
        y += h
    besselFuncs.append(y)

besselFuncs = np.array(besselFuncs)
fig = plt.figure()
'''
for i in range(n):
    plt.plot(x, besselFuncs[i])
'''
ax = []
ax.append(fig.add_subplot(111, xlim=(0, 15), ylim=(-0.7, 1)))
ax.append(fig.add_subplot(111, xlim=(0, 15), ylim=(-0.7, 1)))


lines = []


lines.append(ax[0].plot([], [], lw=2))
#lines.append(ax[1].plot([], [], lw=2))

line1, = ax[0].plot([], [], lw=2)


def init():
    lines[0].set_data([], [])
    '''
    lines[1].set_data([], [])
    '''
    line1.set_data([], [])
    return lines,


def animate(i):
    global n, besselFuncs, x
    '''
    lines[0].set_data(x[:i], besselFuncs[2, :i])
    lines[1].set_data(x[:i], besselFuncs[3, :i])
    return lines
    '''
    lines[0].set_data(x[:i], besselFuncs[0, :i])
    return lines,


anim = FuncAnimation(fig, animate, init_func=init, frames=10000, interval=1, blit=True)


anim.save('basic_animation.mp4', fps=3, extra_args=['-vcodec', 'libx264'])


plt.show()