import pandas as pd
import numpy as np

# Question 1
list_1 = [-1, 2, 3, 9, 0]
list_2 = [1, 2, 7, 10, 14]
print(list_1 + list_2)

# Question 2
list_1=[-1, 2, 3, 9, 0]
list_2=[1, 2, 7, 10, 14]

# implementing using a for loop
# iterate through both lists
#add list_1[i] and list_2[i] 
sum = []
for i in range (0, len(list_1)):
    sum.append(list_1[i] + list_2[i])

print(sum)  

# Question 3
# Question 3 
# creating a 4D ndarray
# when .shape is printed the shape is (2, 3, 2, 1)
# this means the x axis has a length of 2, y axis has a height of 3, and a z width of 2
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
    ]
    ])
print(my_4D_array.shape)

# Question 4 using np.arange and .reshape create a 3D array which looks like the array below
# it should only have 1 line of code 

my_2d_array = np.arange(27).reshape(3,3,3)
#print(my_2d_array)

# now we want to get the first column of each matrix 
# we know to get an entire column we use print(my_2d_array[:, 2])

print(my_2d_array[:, : , 0])

# remember ':' means everything in that row or column 
# so for every row in every matrix that is in the index 0 we print it out

# our next task is to get the middle matrix and the middle row 

print(my_2d_array[1, 1, :])

# this works because it is the 2nd matrix leading to a value of 1
# and it is the 2nd row we want hence the 1 in the next column
# and we want to select all the values making us use ':'

# our next task is taking all of the edge pieces
print(my_2d_array[:, ::2, ::2])
# the :: is used since we know that it is used to skip certain values 

# Question 5

my_3d_array = np.arange(27).reshape(3,3,3)
#print(my_3d_array)

# accessing 4, 17 and 18
print(my_3d_array[[0, 1, 2], [1, 2, 0], [1, 2, 0]])

# accessing 9 and 17
print(my_3d_array[[1, 1], [0, 2], [0, 2]])

# Question 6 
my_2d_array = np.arange(-10, 20).reshape(5,6)

sum_of_cols = my_2d_array.sum(axis=0)

indexing_array = sum_of_cols % 10 == 0

print(my_2d_array[:, indexing_array])
