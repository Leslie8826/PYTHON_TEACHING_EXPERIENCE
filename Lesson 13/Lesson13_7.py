
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print ("Array a: \n", a)
print("\n")

# Each element of first dimension is paired with the element of the second 
# dimension. In this case, the index of the elements are (0,0),(1,1),(2,0)
# and the corresponding elements are displayed.
print("Example 1: Displaying elements (0,0), (1,1) and (2,0) with integer array indexing method: ")
print(a[[0, 1, 2], [0, 1, 0]])  

# The above example of integer array indexing is equivalent to this:
print("\n Example 1 is equivalent to the following: ")
print(np.array([a[0, 0], a[1, 1], a[2, 0]])) 

# It is possible to reuse the same element from the source array, when 
# using integer array indexing
print("\n Example 2: ")
print(a[[0, 0], [1, 1]]) 

# Equivalent to the previous integer array indexing example
print("\n Equivalent to example 2:")
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"




##################
##### Output #####
##################
Array a: 
 [[1 2]
 [3 4]
 [5 6]]

Example 1: Displaying elements (0,0), (1,1) and (2,0) with integer array indexing method: 
[1 4 5]

 Example 1 is equivalent to the following: 
[1 4 5]

 Example 2: 
[2 2]

 Equivalent to example 2:
[2 2]
