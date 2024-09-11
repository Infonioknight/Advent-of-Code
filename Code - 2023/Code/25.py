import networkx as nx

# data = open('Test.txt', 'r').read().split('\n')
data = open("Connections.txt", 'r').read().split('\n')

g = nx.Graph()
for line in data:
    s, d = line.split(':')
    for item in d.strip().split(' '):
        g.add_edge(s, item)
        g.add_edge(item, s)

for pair in nx.minimum_edge_cut(g):
    g.remove_edge(pair[0], pair[1])

a, b = nx.connected_components(g)
print(len(a) * len(b))