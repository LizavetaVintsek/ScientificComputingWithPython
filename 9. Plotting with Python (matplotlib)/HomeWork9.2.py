import matplotlib.pyplot as plt
import numpy as np
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
area = [50*(x+y)]
colors = np.where(x**2 + y**2 < 1, 'g', 'r')
plt.scatter(x, y, c=colors, s=area)
plt.show()
