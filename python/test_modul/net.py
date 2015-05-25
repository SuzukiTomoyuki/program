import networkx as nx
import matplotlib.pylab as plt

if __name__ == '__main__':
	g = nx.Graph()
	g.add_nodes_from(['node1','node2','node3'])
	g.add_node('node4')

	g.add_edge('node1','node2')
	g.add_edges_from([('node1','node3'),('node2','node4')])

	print g.nodes(),g.edges()

	nx.draw_networkx(g)
	plt.savefig("sample.png")