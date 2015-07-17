# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import colorsys

if __name__ == '__main__':
	sample = nx.cubical_graph()

	for i in xrange(0,50):
		sample.add_node(i)

	for i in xrange(0,50):
		sample.add_edge(i,poisson(lam=30))
	#print sample.edges()
	try: print nx.shortest_path(sample, 30, 0)
	except: print u"ぼっち"
    #graph layput
    #circular, random, shell, spring, spectral
    #ncolors = [colorsys.hsv_to_rgb(h / num_nodes, 1.0, 1.0)for h in range(num_nodes)]
	nx.draw(sample, pos=nx.spring_layout(sample), node_color='white',edge_color="g")

	plt.savefig("sample.png")
	nx.write_gexf(sample, "sample.gexf")