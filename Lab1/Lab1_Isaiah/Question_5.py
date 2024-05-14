# Question 5

import numpy as np

a = np.arange(27).reshape(3,3,3)
print(a[[2,1,0],[0,2,1],[0,2,1]])

print(a[[1,1],[0,2],[0,2]])