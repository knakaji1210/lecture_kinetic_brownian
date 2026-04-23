# Function to draw animation of 3d Random Walk (Cube Lattice model)
# 260401 2dをベースに3dに拡張

import random as rd
import numpy as np
from math import *

def randomWalk_3dCubeLattice(N):

    num = 0
    x, y, z = 0, 0, 0
    coordinate_list = [[x,y,z]]
    direction_list = ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

    for i in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        z = z + step[2]
        coordinate = [x, y, z]
        coordinate_list.append(coordinate)
        num = num + 1
#    print("final num = {0}".format(num))    # to check the number of steps
    return coordinate_list

def coordinateList2xyzList(coordinate_list, N):
    x_list = [ coordinate_list[i][0] for i in range(N+1) ]
    y_list = [ coordinate_list[i][1] for i in range(N+1) ]
    z_list = [ coordinate_list[i][2] for i in range(N+1) ]

    x_array = np.asanyarray(x_list, dtype=object)  # 付加的にこれもndarrayに変換
    y_array = np.asanyarray(y_list, dtype=object)  # 付加的にこれもndarrayに変換
    z_array = np.asanyarray(z_list, dtype=object)  # 付加的にこれもndarrayに変換

    return x_array, y_array, z_array

def xyzList2xyzStep(xyzlist, N):
    xyzlist_steps = [ xyzlist[:i] for i in range(N+2) ]
    xyzlist_steps = xyzlist_steps[1:]

    # numpyのバージョンアップにより、""ndarray from ragged nested sequences"の制限が厳しくなり、
    # animatplotの途中でエラーが出るようになった。そのための修正が以下の１行
    xyzarray_steps = np.asanyarray(xyzlist_steps, dtype=object)

    return xyzarray_steps # 同じ理由でここも変更

def tlistStep(N):
    t_list = np.arange(0,N+1)
    tlist_steps = [ t_list[:i].tolist() for i in range(N+2) ]
    tlist_steps = tlist_steps[1:]

    # animatplotの途中でエラーが出るようになった。そのための修正が以下の１行
    tarray_steps = np.asanyarray(tlist_steps, dtype=object)

    return tarray_steps

# 距離（使っていない）
def distFromOrigin(x_list, y_list, N):
    d_list = [ np.sqrt(x**2 + y**2) for x, y in zip(x_list, y_list)]
    dlist_steps = [ d_list[:i] for i in range(N+2) ]
    dlist_steps = dlist_steps[1:]
    return d_list, dlist_steps

# 距離の二乗
def dist2FromOrigin(x_list, y_list, z_list, N):
    d2_list = [ x**2 + y**2 + z**2 for x, y, z in zip(x_list, y_list, z_list)]
    d2list_steps = [ d2_list[:i] for i in range(N+2) ]
    d2list_steps = d2list_steps[1:]

    # animatplotの途中でエラーが出るようになった。そのための修正が以下の２行
    d2_array = np.asanyarray(d2_list, dtype=object)
    d2_array_steps = np.asanyarray(d2list_steps, dtype=object)

    return d2_array, d2_array_steps

#　使っていない
def coordinateList2coordinateStep(coordinate_list, N):
    coordinate_list_steps = [ coordinate_list[:i] for i in range(N) ]
    coordinate_list_steps = coordinate_list_steps[1:]
    return coordinate_list_steps

def calcMeanDist2(d2_list_repeat, N, M):
    d2_mean_list = []
    for i in range(N+1):
        d2_rep_list = [ d2_list_repeat[j][i] for j in range(M) ]
        d2_mean = np.mean(d2_rep_list)
        d2_mean_list.append(d2_mean)
    return d2_mean_list