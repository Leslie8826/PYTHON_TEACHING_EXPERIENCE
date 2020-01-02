# This program plots points according to their coordinates
# It chooses a certain type of plots to display the points
# The x axis goes from 0 to 6
# The y axis goes from 0 to 20
import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,4,9,16], 'ro') # coordinates of points
plt.axis([0, 6, 0, 20]) # axis dimensions
plt.show()
