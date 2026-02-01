# Animation of 1d Random Walk (Square Lattice model)

# 描いている軌跡と同時にMSDを計算するバージョン

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import brownianFunc_1d_v1 as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

plot_lim = 2*np.sqrt(N)
t = np.linspace(0, N, N+1)
t_max = np.max(t)

coordinate_list = brw.randomWalk_1dSquareLattice(N)
x_array, y_array = brw.coordinateList2xyList(coordinate_list, N)

x_array_steps = brw.xyList2xyStep(x_array, N)
y_array_steps = brw.xyList2xyStep(y_array, N)

t_array_steps = brw.tlistStep(N)

d2_array, d2_array_steps = brw.dist2FromOrigin(x_array, N)
fig_title1 = "1-dimensional Brownian Motion ($N$ = {0})".format(N)
fig_title2 = "Mean Square Displacement, <$d^{{2}}$> vs $t$"

fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(121, title=fig_title1, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax1.grid(axis='both', color="gray", lw=0.5)

randomWalk = amp.blocks.Line(x_array_steps, y_array_steps, ax=ax1, ls='-', marker="o", markersize=100/plot_lim, color='blue')

ax2 = fig.add_subplot(122, title=fig_title2, xlabel='$t$', ylabel='<$d^{{2}}$>',
        xlim=[0, t_max], ylim=[0 , t_max])
ax2.grid(axis='both', color="gray", lw=0.5)

# Theoretically <x^2> = 2Dt = t since D = 1/2
ax2.plot(t, t, ls='--', color="gray", lw=0.5)

dist2Origin = amp.blocks.Scatter(t_array_steps, d2_array_steps, ax=ax2, marker="o", s=300/plot_lim, color='red')

timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([randomWalk, dist2Origin], timeline)
anim.controls()

savefile = "./gif/Brownian_Motion_1d_{0}steps_with_MSD_ani".format(N)
anim.save_gif(savefile)

plt.show()
plt.close()
