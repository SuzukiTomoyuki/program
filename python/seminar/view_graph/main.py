import Graph

if __name__=='__main__':
	graph1=Graph.Graph('nokogiri')
	graph1.write_graph()
	graph1.__init__('cos')
	graph1.write_graph()
	graph1.__init__('sin')
	graph1.write_graph()
