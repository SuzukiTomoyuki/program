# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *

if __name__ == '__main__':
	g = nx.Graph()
	g.add_nodes_from(['node1','node2','node3'])
	g.add_node('node4')

	g.add_edge('node1','node2')
	g.add_edges_from([('node1','node3'),('node2','node4')])

	sample = nx.Graph()

	for i in xrange(0,60):
		sample.add_node(i)

	for i in xrange(0,60):
		sample.add_edge(i,poisson(lam=30))
	#print sample.edges()
	try: print nx.shortest_path(sample, 30, 0)
	except: print u"ぼっち"
	nx.draw_networkx(sample)
	plt.savefig("sample.png")