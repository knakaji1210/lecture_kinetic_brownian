# Animation of 3d Random Walk (Cube Lattice model)
# 260401 2dをベースに3dに拡張

import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp
import brownianFunc_3d_v2 as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

plot_lim = 3*np.sqrt(N)
t = np.linspace(0, N, N+1)

coordinate_list = brw.randomWalk_3dCubeLattice(N)
x_list, y_list, z_list = brw.coordinateList2xyzList(coordinate_list, N)

x_array_steps = brw.xyzList2xyzStep(x_list, N)
y_array_steps = brw.xyzList2xyzStep(y_list, N)
z_array_steps = brw.xyzList2xyzStep(z_list, N)

fig_title = "3-dimensional Brownian Motion ($N$ = {0})".format(N)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$X$', ylabel='$Y$',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

#randomWalk = amp.blocks.Line(x_array_steps, y_array_steps, ax=ax, ls='-', marker="o", markersize=100/plot_lim, color='blue')
#randomWalk = amp.blocks.Line(y_array_steps, z_array_steps, ax=ax, ls='-', marker="o", markersize=100/plot_lim, color='blue')
randomWalk = amp.blocks.Line(z_array_steps, x_array_steps, ax=ax, ls='-', marker="o", markersize=100/plot_lim, color='blue')

timeline = amp.Timeline(t, units=' steps', fps=30)

anim = amp.Animation([randomWalk], timeline)
anim.controls()

savefile = './mp4/Brownian_Motion_3d_{0}steps.mp4'.format(N)
anim.save(savefile, writer='ffmpeg', fps=30, extra_args=['-r', '30'])

plt.show()
plt.close()
