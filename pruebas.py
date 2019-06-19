import networkx as nx              # importing networkx package
from matplotlib.pyplot import show

x1=int(input("Escriba el valor x del primer punto:"))
y1=int(input("EEscriba el valor y del primer punto:"))
x2=int(input("Escriba el valor x del segudo punto:"))
y2=int(input("EEscriba el valor y del segudo punto:"))

G = nx.Graph()
G.add_edges_from([(x1, y1), (x2, y2)])

nx.draw(G)
show()