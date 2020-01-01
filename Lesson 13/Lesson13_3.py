# This program creates different types of array
# using numpy built-in functions


import numpy as np

# Create an array of all zeros
a = np.zeros((2,2))   
print("Array of all zeros: \n", a)              
  
print("\n")      # add space after this array

# Create an 1-rank array of all ones
b = np.ones((1,2))    
print("1-rank array of all ones: \n", b)              

print("\n")      # add space after this array

# Create a constant array filled with values 7
c = np.full((2,2), 7)  
print("Constant array: \n", c)               
  
print("\n")      # add space after this array

# Create a 2x2 identity matrix
d = np.eye(2)         
print("Create a 2x2 identity matrix: \n", d)              

print("\n")      # add space after this array

# Create an array filled with random values
e = np.random.random((2,2))  
print("Create an array filled with random values: \n", e)    






##################
##### Output #####
##################

2-rank array of all zeros: 
 [[0. 0.]
 [0. 0.]]


1-rank array of all ones: 
 [[1. 1.]]


Constant array: 
 [[7 7]
 [7 7]]


Create a 2x2 identity matrix: 
 [[1. 0.]
 [0. 1.]]


Create an array filled with random values: 
 [[0.90638689 0.89978339]
 [0.23392159 0.06164558]]
