# This progran make a few elementwise computations
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print("Array x: \n", x)
print("\n Array y: \n", y)

# Elementwise sum
print("\n Two ways to compute a addition: ")
print("x + y = \n", x + y)
print("\n np.add(x, y) = \n", np.add(x, y))

# Elementwise difference
print("\n Two ways to compute a subtraction: ")
print("x - y = \n", x - y)
print("\n np.subtract(x, y) = \n", np.subtract(x, y))

# Elementwise product
print("\n Two ways to compute a product: ")
print("x * y = \n", x * y)
print("\n np.multiply(x, y) = \n", np.multiply(x, y))

# Elementwise division
print("\n Two ways to compute a division: ")
print("x / y = \n", x / y)
print("\n np.divide(x, y) = \n", np.divide(x, y))

# Elementwise square root
print("\n Square root of array x:")
print(np.sqrt(x))




##################
##### Output #####
##################
Array x: 
 [[1. 2.]
 [3. 4.]]

 Array y: 
 [[5. 6.]
 [7. 8.]]

 Two ways to compute a addition: 
x + y = 
 [[ 6.  8.]
 [10. 12.]]

 np.add(x, y) = 
 [[ 6.  8.]
 [10. 12.]]

 Two ways to compute a subtraction: 
x - y = 
 [[-4. -4.]
 [-4. -4.]]

 np.subtract(x, y) = 
 [[-4. -4.]
 [-4. -4.]]

 Two ways to compute a product: 
x * y = 
 [[ 5. 12.]
 [21. 32.]]

 np.multiply(x, y) = 
 [[ 5. 12.]
 [21. 32.]]

 Two ways to compute a division: 
x / y = 
 [[0.2        0.33333333]
 [0.42857143 0.5       ]]

 np.divide(x, y) = 
 [[0.2        0.33333333]
 [0.42857143 0.5       ]]

 Square root of array x:
[[1.         1.41421356]
 [1.73205081 2.        ]]
