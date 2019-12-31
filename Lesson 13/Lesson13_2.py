# This program 

import numpy as np

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array

# Displays the shape of matrix b
print("Shape of matrix b: \n", b.shape)  

# Displays the elements at some indexes in the array
print("\n Elements at index [0, 0], [0, 1] and [1, 0]: \n", b[0, 0], b[0, 1], b[1, 0]) 


##################
##### Output #####
##################
Shape of matrix b: 
(2, 3)

Elements at index [0, 0], [0, 1] and [1, 0]: 
1 2 4
