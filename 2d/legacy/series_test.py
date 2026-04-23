import numpy as np

x_list = np.arange(0,11)

x_list_step = [ x_list[:i].tolist() for i in range(12) ]
x_list_step = x_list_step[1:]

print(x_list_step)