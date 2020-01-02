
import numpy as np

x = np.array([1, 2]) # Let numpy choose the datatype
print("Array x: \n", x)   
print("Datatype of elements of x: \n", x.dtype)         

y = np.array([1.0, 2.0])   # Let numpy choose the datatype
print("\n Array y: \n", y)
print(" Datatype of elements of y: \n", y.dtype)             

z = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
print("\n Array z: \n", z)
print("Datatype of elements of z: \n", z.dtype)  


##################
##### Output #####
##################
Array x: 
 [1 2]
Datatype of elements of x: 
 int64

 Array y: 
 [1. 2.]
 Datatype of elements of y: 
 float64

 Array z: 
 [1 2]
Datatype of elements of z: 
 int64
