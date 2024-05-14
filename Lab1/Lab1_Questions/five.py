import pandas as pd
import numpy as np

my_3d_array = np.arange(27).reshape(3,3,3)
#print(my_3d_array)

# accessing 4, 17 and 18
print(my_3d_array[[0, 1, 2], [1, 2, 0], [1, 2, 0]])

# accessing 9 and 17
print(my_3d_array[[1, 1], [0, 2], [0, 2]])