import numpy as np
filename = 'control_test.txt'
data = np.loadtxt(filename, delimiter=' ', dtype=float, usecols= (3, 4, 5, 6))
print(data)