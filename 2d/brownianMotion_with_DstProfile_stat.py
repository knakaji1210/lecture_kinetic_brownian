# Statistics of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
import brownianFunc as brw

try:
    N = int(input('Number of steps (default=100): '))
except ValueError:
    N = 100

try:
    M = int(input('Number of repeat (default=100): '))
except ValueError:
    M = 100

t = np.linspace(0, N, N+1)
t_max = np.max(t)

d2_list_repeat = []

for i in range (M):
    coordinate_list = brw.randomWalk_2dSquareLattice(N)
    x_list, y_list = brw.coordinateList2xyList(coordinate_list, N)
    d2_list, d2_list_steps = brw.dist2FromOrigin(x_list, y_list, N)
    d2_list_repeat.append(d2_list)
    
d2_mean_list = brw.calcMeanDist2(d2_list_repeat, N, M)

fig_text1 = "Number of steps: {}".format(N)
fig_text2 = "Number of repetition: {}".format(M)

fig_title = "<$d^{{2}}$> vs $t$"

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, title=fig_title, xlabel='$t$', ylabel='<$d^{{2}}$>',
        xlim=[0, t_max], ylim=[0 , t_max])
ax.grid(axis='both', color="gray", lw=0.5)

# Theoretically <x^2> = <2Dt> = <t> since D = 1/2
ax.plot(t, t, ls='--', color="gray", lw=0.5)

# MSD
ax.scatter(t, d2_mean_list, marker="o", color="red")

fig.text(0.15, 0.8, fig_text1)
fig.text(0.15, 0.75, fig_text2)

savefile = "./gif/Brownian_Motion_N{0}_M{1}".format(N, M)
fig.savefig(savefile, dpi=300)

plt.show()
plt.close()
