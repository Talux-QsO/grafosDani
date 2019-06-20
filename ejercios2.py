#libreiras inportadas
from matplotlib.pyplot import show
import networkx as nx
#cantidad de nodos
nodos=int(input("numero de nodos:"))
#dibujo
G = nx.path_graph(nodos)
nx.draw(G)
show()
