import networkx as nx
import matplotlib.pyplot as plt

# Initiating an empty Graph object
P = nx.Graph()  # create an empty object

# You can add nodes using add_nodes_from()
P.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Use add_edges_from to add pairwise relationships
edge = ('B', 'C')
edges = [edge, ('A', 'C'), ('B', 'D'), ('D', 'A'), ('D', 'E'), ('B', 'E')]
P.add_edges_from(edges)

print(P.nodes())
print(P.edges())
print(type(edge))
print(type(edges))

nx.draw(P, with_labels=True)
plt.show()

G = nx.path_graph(8)
nx.draw(G)
plt.show()