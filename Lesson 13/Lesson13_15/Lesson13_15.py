# This program creates an array of speeds and plot them 
# according to moves ranks
import numpy as np
import matplotlib.pyplot as plt

speed = np.array([1, 6, 4, 15, -6, 3])

plt.plot(speed)
plt.ylabel('Speed')
plt.xlabel('Moves')
plt.show()


##################
##### Output #####
##################
# see numpy_matplotlib2.png to visualize the plot
