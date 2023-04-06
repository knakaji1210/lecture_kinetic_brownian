# Function to draw animation of 2d Random Walk (Square Lattice model)

import random as rd
import numpy as np
from math import *

def randomWalk_2dSquareLattice(N):

    num = 0
    x, y = 0, 0
    coordinate_list = [[x,y]]
    direction_list = ([1,0],[-1,0],[0,1],[0,-1])

    for i in range(N):
        step = rd.choice(direction_list)
        x = x + step[0]
        y = y + step[1]
        coordinate = [x, y]
        coordinate_list.append(coordinate)
        num = num + 1
#    print("final num = {0}".format(num))    # to check the number of steps
    return coordinate_list

def coordinateList2xyList(coordinate_list, N):
    x_list = [ coordinate_list[i][0] for i in range(N+1) ]
    y_list = [ coordinate_list[i][1] for i in range(N+1) ]
    return x_list, y_list

def xyList2xyStep(xylist, N):
    xylist_steps = [ xylist[:i] for i in range(N+2) ]
    xylist_steps = xylist_steps[1:]
    return xylist_steps

def tlistStep(N):
    t_list = np.arange(0,N+1)
    tlist_steps = [ t_list[:i].tolist() for i in range(N+2) ]
    tlist_steps = tlist_steps[1:]
    return tlist_steps

# 距離（使っていない）
def distFromOrigin(x_list, y_list, N):
    d_list = [ np.sqrt(x**2 + y**2) for x, y in zip(x_list, y_list)]
    dlist_steps = [ d_list[:i] for i in range(N+2) ]
    dlist_steps = dlist_steps[1:]
    return d_list, dlist_steps

# 距離の二乗
def dist2FromOrigin(x_list, y_list, N):
    d2_list = [ x**2 + y**2 for x, y in zip(x_list, y_list)]
    d2list_steps = [ d2_list[:i] for i in range(N+2) ]
    d2list_steps = d2list_steps[1:]
    return d2_list, d2list_steps

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