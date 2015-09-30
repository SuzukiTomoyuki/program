# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
import treetaggerwrapper

def main():
	# init
	tagger = treetaggerwrapper.TreeTagger(TAGLANG='en',TAGDIR='/Users/suzukitoshiyuki/Applications/tree_tagger')
	file_path = '/Users/suzukitoshiyuki/program/complexnetwork/movies.txt'
	count = 0
	G = nx.Graph()

	f = open(file_path)
	line = f.readline()

	while count < 1000:
		if line.find('product/productId:') != -1:
			product_name = line.split(':')[1]

		if line.find('review/text:') != -1:
			count = 1 + count
			# 単語分割
			tags = tagger.TagText(line.split(':')[1])
			for tag in tags:
				try:
					mm = tag.split('\t')
					if mm[1] == 'NN':
						if mm[2] != '<unknown>':
							G.add_edge(product_name, mm[2])
				except:
					pass
		else:
			pass
		line = f.readline()

	d=nx.degree(G)
	pos = nx.spring_layout(G)
	plt.figure(figsize = (15, 15))
	nx.draw_networkx_nodes(G, pos, nodelist=d.keys(), node_size=[v * 25 for v in d.values()], node_color = 'b',label=1)    
	nx.draw_networkx_edges(G, pos, width = 1)
	nx.draw_networkx_labels(G, pos, font_size = 1, font_family = 'sans-serif', font_color = 'r')
	plt.savefig("movies.png")

if __name__ == '__main__':
	main()