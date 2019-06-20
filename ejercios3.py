import matplotlib.pyplot as plt
import networkx as nx

var=int(input("Numero de nodos:"))

G = nx.star_graph(var)
pos = nx.spring_layout(G)
colors = range(var)
nx.draw(G, pos, node_color='#442AA5', edge_color=colors,
        width=3, edge_cmap=plt.cm.Blues, with_labels=True)
plt.show()

