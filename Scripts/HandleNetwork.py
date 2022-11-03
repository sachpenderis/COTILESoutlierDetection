import networkx as nx


dataset = open("../Datasets/NetworkUnix.txt", 'r')

g = nx.Graph()

for line in dataset:
    g.add_edge(int(line.split()[0]), int(line.split()[1]))

print(g.number_of_nodes())
print(g.number_of_selfloops())
