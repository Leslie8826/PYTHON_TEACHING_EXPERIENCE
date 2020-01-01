# This program creates an array, a subarray and assigns a value to the subarray

import numpy as np

# Creates the following rank 2 array with shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print("Array a: \n", a)

# Creates the subarray b of shape (2, 2) consisting of the first 2 rows
# and columns 1 and 2 of array a
b = a[:2, 1:3]
print("\n Array b (subarray of a): \n", b)

# Displays the element that is in (row 0, column 1)
print("\n a[0, 1] = ", a[0, 1])   # Prints "2"

# Assigns element at (row 0, column 0) a new value in array b
# Note: modifying an element in array b will also modifies this element in array a.
#       in array a the element to be modified is at (row 0, column 1)
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]

# Checks if element b[0, 0] and a[0, 1] are the same
print("\n b[0, 0] = ", b[0, 0])
print(" a[0, 1] = ", a[0, 1])   

# Displays array a after new assignement
print("\n Array a after assignment: \n", a)
