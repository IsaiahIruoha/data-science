# Question 6

import numpy as np

a = np.arange(-10,20).reshape(5,6)
print(a)

sum_of_cols = a.sum(axis=0)

indexing_array = sum_of_cols % 10 == 0

print(a[:, indexing_array])