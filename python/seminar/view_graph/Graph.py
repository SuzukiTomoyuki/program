import pylab as pl
import numpy as np
from scipy import signal

class Graph_type(object):
	def __init__(self,graph_type):
		self.graph_type=graph_type
	def write_graph(self):
		pass

class Graph(Graph_type):
	def __init__(self,gr_type):
		super(Graph,self).__init__(gr_type)
	def write_graph(self):	#overwrite
		if self.graph_type is 'nokogiri':

			X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
			Y = signal.sawtooth(X)
			set_graph()
			pl.plot(X,Y)
			pl.savefig('nokogiri.png')
			pl.show()

		elif self.graph_type is 'cos':
			X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
			Y = np.cos(X)
			set_graph()
			pl.plot(X,Y)
			pl.savefig('cos.png')
			pl.show()

		elif self.graph_type is 'sin':
			X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
			Y = np.sin(X)
			set_graph()
			pl.plot(X,Y)
			pl.savefig('sin.png')
			pl.show()

		else: print 'faild'



	def data_nokogiri(self):
		pass


def set_graph():
	pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
	pl.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
	ax = pl.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))