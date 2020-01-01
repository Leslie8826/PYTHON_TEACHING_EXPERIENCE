# This program creates an array and displays some rows 
# and some columns using a mix of integers with slices 
# to access the aforementioned rows and columns

import numpy as np

# Creates a rank 2 array with shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("Array a: \n", a)

# Mixing integer with slices to access rows or columns of an array

# Displays the second row (row 1) of array a in two ways
print("\n Row 1:")
row_r1 = a[1, :]    
row_r2 = a[1:2, :]  
print(row_r1, row_r1.shape)  
print(row_r2, row_r2.shape)  

# Displays column 1 of array a in two ways
print("Column 1: ")
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape) 
print(col_r2, col_r2.shape) 



##################
##### Output #####
##################
Array a: 
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

 Row 1:
[5 6 7 8] (4,)
[[5 6 7 8]] (1, 4)

 Column 1: 
[ 2  6 10] (3,)
[[ 2]
 [ 6]
 [10]] (3, 1)
