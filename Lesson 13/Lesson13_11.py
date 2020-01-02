# This program computes two vectors, two matrices and a vector with a matrix 

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

print("ARRAYS:")
print("Array x: \n", x)
print("\n Array y: \n", y)

print("\n VECTORS:")
print("Vector v: \n", v)
print("\n Vector w: \n", w)


# Inner product of vectors
print("\n Inner product of vectors:")
print("v.dot(w) = ", v.dot(w))
print("np.dot(v, w) = ", np.dot(v, w))

# Matrix/vector product
print("\n Matrix/vector product:")
print("x.dot(v) = ", x.dot(v))
print("np.dot(x, v) = ", np.dot(x, v))

# Matrix / matrix product
print("\n Matrix/matrix product:")
print("x.dot(y) = \n", x.dot(y))
print("\n np.dot(x, y) = \n", np.dot(x, y))






##################
##### Output #####
##################
ARRAYS:
Array x: 
 [[1 2]
 [3 4]]

 Array y: 
 [[5 6]
 [7 8]]

 VECTORS:
Vector v: 
 [ 9 10]

 Vector w: 
 [11 12]

 Inner product of vectors:
v.dot(w) =  219
np.dot(v, w) =  219

 Matrix/vector product:
x.dot(v) =  [29 67]
np.dot(x, v) =  [29 67]

 Matrix/matrix product:
x.dot(y) = 
 [[19 22]
 [43 50]]

 np.dot(x, y) = 
 [[19 22]
 [43 50]]
