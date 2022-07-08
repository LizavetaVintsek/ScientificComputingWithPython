import networkx as nx

import matplotlib.pyplot as plt

regular = nx.random_regular_graph(d=5, n=10)
nx.draw(regular)
plt.show()
