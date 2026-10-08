import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = input("Enter nodes:").split(",")
G.add_nodes_from(nodes)

edges = input("Enter edges (a-b):").split(",")
for e in edges:
    a,b = e.strip().split("-")
    G.add_edge(a,b)
nx.draw(G,with_labels = True, node_size = 800, arrows = True )
plt.show()
