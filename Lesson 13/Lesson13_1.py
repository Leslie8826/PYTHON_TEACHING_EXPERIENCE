# This program creates an array and 
# display some information

import numpy as np

# Creates a rank 1 array
a = np.array([1, 2, 3])   
#a = np.array([[1, 2], [5, 8], [888, 999]])   
print("a =", a)

# Displays the type of a
print("\n Type of a: \n", type(a))    

# Shape of a
print("\n Shape of a: \n", a.shape)          

# Printing elements at certain indexes in array
print("\n Index of : \n", a[0], a[1], a[2])

# Change the element at index 0 in the array and prints it
a[0] = 5  
print("\n Array a after new assignment: \n", a)  



##################
##### Output #####
##################
a = [1 2 3]

 Type of a: 
 <class 'numpy.ndarray'>

 Shape of a: 
 (3,)

 Index of : 
 1 2 3

 Array a after new assignment: 
 [5 2 3]
