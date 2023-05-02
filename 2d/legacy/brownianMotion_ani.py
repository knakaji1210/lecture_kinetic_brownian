# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import brownianFunc as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

plot_lim = 3*np.sqrt(N)
t = np.linspace(0, N, N+1)

coordinate_list = brw.randomWalk_2dSquareLattice(N)
x_list, y_list = brw.coordinateList2xyList(coordinate_list, N)

x_list_steps = brw.xyList2xyStep(x_list, N)
y_list_steps = brw.xyList2xyStep(y_list, N)

fig_title = "2-dimensional Random Walk ($N$ = {0})".format(N)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(x_list_steps, y_list_steps, ax=ax, ls='-', marker="o", markersize=100/plot_lim, color='blue')

timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([randomWalk], timeline)
anim.controls()

savefile = "./gif/Brownian_Motion_{0}steps".format(N)
anim.save_gif(savefile)

plt.show()
plt.close()
