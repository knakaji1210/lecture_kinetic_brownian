# Function to draw animation of 1d Random Walk (Square Lattice model)

# 2dから移植

import random as rd
import numpy as np
from math import *

def randomWalk_1dSquareLattice(N):

    num = 0
    x = 0
    coordinate_list = [[x,0]]
    direction_list = ([1,0],[-1,0])

    for i in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        coordinate = [x, 0]
        coordinate_list.append(coordinate)
        num = num + 1
#    print("final num = {0}".format(num))    # to check the number of steps
    return coordinate_list

def coordinateList2xyList(coordinate_list, N):
    x_list = [ coordinate_list[i][0] for i in range(N+1) ]

    x_array = np.asanyarray(x_list, dtype=object)  # 付加的にこれもndarrayに変換

    return x_array

def xList2xStep(xlist, N):
    xlist_steps = [ xlist[:i] for i in range(N+2) ]
    xlist_steps = xlist_steps[1:]

    # numpyのバージョンアップにより、""ndarray from ragged nested sequences"の制限が厳しくなり、
    # animatplotの途中でエラーが出るようになった。そのための修正が以下の１行
    xarray_steps = np.asanyarray(xlist_steps, dtype=object)

    return xarray_steps # 同じ理由でここも変更

def tlistStep(N):
    t_list = np.arange(0,N+1)
    tlist_steps = [ t_list[:i].tolist() for i in range(N+2) ]
    tlist_steps = tlist_steps[1:]

    # animatplotの途中でエラーが出るようになった。そのための修正が以下の１行
    tarray_steps = np.asanyarray(tlist_steps, dtype=object)

    return tarray_steps

# 距離（使っていない）
def distFromOrigin(x_list, N):
    d_list = [ np.sqrt(x**2) for x in x_list]           # x_listと同じものになるね
    dlist_steps = [ d_list[:i] for i in range(N+2) ]
    dlist_steps = dlist_steps[1:]
    return d_list, dlist_steps

# 距離の二乗
def dist2FromOrigin(x_list, N):
    d2_list = [ x**2 for x in x_list ]
    d2list_steps = [ d2_list[:i] for i in range(N+2) ]
    d2list_steps = d2list_steps[1:]

    # animatplotの途中でエラーが出るようになった。そのための修正が以下の２行
    d2_array = np.asanyarray(d2_list, dtype=object)
    d2_array_steps = np.asanyarray(d2list_steps, dtype=object)

    return d2_array, d2_array_steps


def calcMeanDist2(d2_list_repeat, N, M):
    d2_mean_list = []
    for i in range(N+1):
        d2_rep_list = [ d2_list_repeat[j][i] for j in range(M) ]
        d2_mean = np.mean(d2_rep_list)
        d2_mean_list.append(d2_mean)
    return d2_mean_list