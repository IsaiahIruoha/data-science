import pandas as pd
import numpy as np

# Question 4 using np.arange and .reshape create a 3D array which looks like the array below
# it should only have 1 line of code 

my_2d_array = np.arange(27).reshape(3,3,3)
# print(my_2d_array)

# now we want to get the first column of each matrix 
# we know to get an entire column we use print(my_2d_array[:, 2])

# print(my_2d_array[:, : , 0])

# remember ':' means everything in that row or column 
# so for every row in every matrix that is in the index 0 we print it out

# our next task is to get the middle matrix and the middle row 

# print(my_2d_array[1, 1, :])

# this works because it is the 2nd matrix leading to a value of 1
# and it is the 2nd row we want hence the 1 in the next column
# and we want to select all the values making us use ':'

# our next task is taking all of the edge pieces

print(my_2d_array[:, ::2, ::2])

# the :: is used since we know that it is used to skip certain values 
# and this applied for all the arrays so we use ':' in the first index 


