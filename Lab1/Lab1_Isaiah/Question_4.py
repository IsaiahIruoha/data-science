# Question 4

import numpy as np

a = np.arange(27).reshape(3,3,3)

print(a[:, :, 0])

print(a[1, 1, :])

print(a[:, ::2, ::2])

