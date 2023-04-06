# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import brownianFunc as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

plot_lim = 2*np.sqrt(N)
t = np.linspace(0, N, N+1)
t_max = np.max(t)

coordinate_list = brw.randomWalk_2dSquareLattice(N)
x_list, y_list = brw.coordinateList2xyList(coordinate_list, N)

x_list_steps = brw.xyList2xyStep(x_list, N)
y_list_steps = brw.xyList2xyStep(y_list, N)

t_list_steps = brw.tlistStep(N)

d2_list, d2_list_steps = brw.dist2FromOrigin(x_list, y_list, N)

fig_title1 = "2-dimensional Random Walk ($N$ = {0})".format(N)
fig_title2 = "$d^{{2}}$ vs $t$"

fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(121, title=fig_title1, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax1.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(x_list_steps, y_list_steps, ax=ax1, ls='-', marker="o", markersize=100/plot_lim, color='blue')

ax2 = fig.add_subplot(122, title=fig_title2, xlabel='$t$', ylabel='$d^{{2}}$',
        xlim=[0, t_max], ylim=[0 , t_max])
ax2.grid(axis='both', color="gray", lw=0.5)

# Theoretically <x^2> = <2Dt> = <t> since D = 1/2
ax2.plot(t, t, ls='--', color="gray", lw=0.5)

dist2Origin = amp.blocks.Scatter(t_list_steps, d2_list_steps, ax=ax2, marker="o", s=300/plot_lim, color='red')

timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([randomWalk, dist2Origin], timeline)
anim.controls()

savefile = "./gif/Brownian_Motion_{0}steps".format(N)
anim.save_gif(savefile)

plt.show()
plt.close()
