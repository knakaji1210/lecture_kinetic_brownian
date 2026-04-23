# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import brownianFunc_1d_v0 as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

plot_lim = 3*np.sqrt(N)
t = np.linspace(0, N, N+1)
t_max = np.max(t)

coordinate_list = brw.randomWalk_1dSquareLattice(N)
x_list = brw.coordinateList2xyList(coordinate_list, N)

t_array_steps = brw.tlistStep(N)
x_array_steps = brw.xList2xStep(x_list, N)

fig_title = "1-dimensional Random Walk ($N$ = {0})".format(N)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[0, t_max], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(t_array_steps, x_array_steps, ax=ax, ls='-', marker="o", markersize=100/plot_lim, color='blue')

timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([randomWalk], timeline)
anim.controls()

savefile = "./gif/Brownian_Motion_1d_{0}steps".format(N)
anim.save_gif(savefile)

plt.show()
plt.close()
