import Graph

def main():
	graph1=Graph.Graph('nokogiri')
	graph1.set_graph()
	graph1.graph()
	graph1.write_graph()
	graph1.__init__('cos')
	graph1.set_graph()
	graph1.graph()
	graph1.write_graph()
	graph2=Graph.Graph('sin')
	graph2.set_graph()
	graph2.graph()
	graph2.write_graph()

if __name__=='__main__':
	main()
