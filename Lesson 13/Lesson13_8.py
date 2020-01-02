
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])
print("Array a: \n ", a)

# The following returns a numpy array of Booleans of the same
# shape as array a, where each slot of bool_idx tells
# whether that element of a is greater than 2.
print("\n Array of boolean")
bool_idx = (a > 2)   
print(bool_idx)     

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx


# The following returns an array of rank 1 consisting of 
# the elements of array a that are greater than 2 only
print("\n Boolean array of true value")
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print("\n Another way to display an array of booleans where all values of array a are freater than 2")
print(a[a > 2])     # Prints "[3 4 5 6]"


##################
##### Output #####
##################
Array a: 
  [[1 2]
 [3 4]
 [5 6]]

 Array of boolean
[[False False]
 [ True  True]
 [ True  True]]

 Boolean array of true value
[3 4 5 6]

 Another way to display an array of booleans where all values of array a are freater than 2
[3 4 5 6]
