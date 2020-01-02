# This program plots sin(x) function for values
# from 0 to 5 with spacing of 0.1 between values
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)



##################
##### Output #####
##################
# see numpy_matplot1.png to visualize the plot
