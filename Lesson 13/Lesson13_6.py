
import numpy as np

# Creates a rank 2 array with shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("Array a: \n", a)

# Mixing integer with slices to access rows or columns of an array

# Displays the second row (row 1) of array a in two ways
print("\n")
row_r1 = a[1, :]    
row_r2 = a[1:2, :]  
print(row_r1, row_r1.shape)  
print(row_r2, row_r2.shape)  

print("\n")  #add space between lines

# Displays column 1 of array a in two ways
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


[5 6 7 8] (4,)
[[5 6 7 8]] (1, 4)


[ 2  6 10] (3,)
[[ 2]
 [ 6]
 [10]] (3, 1)
