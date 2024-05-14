import pandas as pd
import numpy as np

# Question 3 
# creating a 4D ndarray
# when .shape is printed the shape is (2, 3, 2, 1)
# this means is has a length of 2, has a height of 3, and a width of 2, and there is only 1 array 
# since 4d arrays factor the amount of 3x3 arrays 
# should only contain 2 lines of code
my_4D_array = np.array([
    [   
        [[1], [2]], 
        [[3], [4]], 
        [[5], [6]]

     ], [
         [[7], [8]], 
         [[9], [10]], 
         [[11], [12]]
    ],
    
    ])
print(my_4D_array.shape)
