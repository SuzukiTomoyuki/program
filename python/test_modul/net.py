import networkx as nx
from matplotlib import pyplot

if __name__ == '__main__':
	g = nx.Graph()
	g.add_nodes_from(['node1','node2','node3'])
	g.add_node('node4')

	g.add_edge('node1','node2')
	g.add_edges_from([('node1','node3'),('node2','node4')])

	print g.nodes(),g.edges()

	nx.draw(g)
	pyplot.show()