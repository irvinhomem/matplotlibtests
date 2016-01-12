import matplotlib.pyplot as plt
from numpy.matlib import rand

a = rand(100)
b = rand(100)

plt.scatter(a,b)
plt.show()