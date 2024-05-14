import pandas as pd
import numpy as np

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
