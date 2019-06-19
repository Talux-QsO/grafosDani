import networkx as nx              # importing networkx package
from matplotlib.pyplot import show    # importing matplotlib package and pyplot is for displaying the graph on canvas 
b=nx.Graph()
b.add_node('helloworld')
b.add_node(2)
b.add_node(2)
'''Node can be called by any python-hashable obj like string,number etc'''
nx.draw(b)                          #draws the networkx graph containing nodes which are declared till before
show()  # displays the networkx graph on matplotlib canvas