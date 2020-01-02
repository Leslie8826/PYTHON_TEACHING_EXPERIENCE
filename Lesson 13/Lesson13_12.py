# This program uses the sum function to add
# single elements or elements in rows or columns

import numpy as np

x = np.array([[1,2],[3,4]])
print("Array x: \n", x)

# Computes the sum of all elements in array x
print("\n Sum of all elements in array x:")
print(np.sum(x))  

# Computes the sum of each column
print("\n Sum of each column:")
print(np.sum(x, axis=0))  

# Computes sum of each row;
print("\n Sum of each row: ")
print(np.sum(x, axis=1))  




##################
##### Output #####
##################
Array x: 
 [[1 2]
 [3 4]]

 Sum of all elements in array x:
10

 Sum of each column:
[4 6]

 Sum of each row: 
[3 7]
