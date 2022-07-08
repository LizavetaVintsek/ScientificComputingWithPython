import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
plt.plot(x, np.sin(x), color="red", linestyle="solid", label="sin(x)")
plt.plot(x, np.cos(x), color="green", linestyle="dashed", label="cos(x)")
plt.plot(x, np.exp(-x), color="blue", linestyle="dotted", label="exp(-x)")
plt.legend()
plt.show()

