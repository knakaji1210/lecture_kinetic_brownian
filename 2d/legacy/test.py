# Animation of 2d Random Walk (Square Lattice model)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import animatplot as amp

# 2.グラフ領域の作成
fig, axes = plt.subplots(1,2)
# 3. アニメーション要素のリスト
artists = []
for i in range(100):
    x = np.linspace(0, 4*np.pi)
    y = np.sin(x - i/100 * 2*np.pi)
 
    my_line1, = axes[0].plot(x, y,"b")
    my_line2, = axes[1].plot(y, x,"r")
    
    #  アニメーション化する要素をリスト化
    artists.append([my_line1, my_line2])
 
# 4. アニメーション化
anim = animation.ArtistAnimation(fig, artists, interval=10)
plt.show()