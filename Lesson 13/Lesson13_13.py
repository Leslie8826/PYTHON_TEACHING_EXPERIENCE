# This program displays the transpose
# of matrices of different ranks

import numpy as np

x = np.array([[1,2], [3,4]])
print("Array x:\n", x)

print("\n Transpose of array x: \n", x.T) 

# Taking the transpose of a rank 1 array does nothing
v = np.array([1,2,3])
print("\n Array v: \n", v)    
print("\n Transpose of v: \n", v.T)





##################
##### Output #####
##################
Array x:
 [[1 2]
 [3 4]]

Transpose of array x: 
 [[1 3]
 [2 4]]

Array v: 
 [1 2 3]

Transpose of v: 
 [1 2 3]
