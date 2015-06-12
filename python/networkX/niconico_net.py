# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import string

class NiconicoMovie(object):
	def __init__(self, nico_string):
		self.video_id = nico_string[0].split(":")[1]
		self.thread_id = nico_string[1].split(":")[1]
		self.title = nico_string[2].split(":")[1].decode("unicode-escape")
		#self.description = nico_string[3].split(":")[1].decode("unicode-escape")
		#self.thumbnail_url = nico_string[4].split(":",1)[1]
		self.upload_time = nico_string[5].split(":")[1:5]
		self.length = nico_string[6].split(":")[1]
		self.movie_type = nico_string[7].split(":")[1]
		self.size_high = nico_string[8].split(":")[1]
		self.size_low = nico_string[9].split(":")[1]
		self.view_counter = nico_string[10].split(":")[1]
		self.comment_counter = nico_string[11].split(":")[1]
		self.mylist_counter = nico_string[12].split(":")[1]
		self.last_res_body = nico_string[13].split(":")[1].decode("unicode-escape")
		self.tags = []
		# self.tags = {}
		for i in nico_string[15:len(nico_string)]:
			if "tag" in i:
				self.tags.append(i.split(":")[1].translate(string.maketrans("", ""), "}]"))
		# for i,x in enumerate(temp):
		# 	print x
		# 	self.tags[i]=x.decode("unicode-escape")
	def print_list(self):
		print "video_id:"+self.video_id
		print "threed_id:"+self.thread_id
		print "title:"+self.title
		print "description:"+self.description
		print "thumbanil_url:"+self.thumbnail_url
		print "upload_time:"+self.upload_time[0]+":"+self.upload_time[1]+":"+self.upload_time[2]+":"+self.upload_time[3]
		print "length:"+self.length
		print "movie_type:"+self.movie_type
		print "size_high:"+self.size_high
		print "size_low:"+self.size_low
		print "view_counter"+self.view_counter
		print "comment_counter:"+self.comment_counter
		print "mylist_counter:"+self.mylist_counter
		print "last_res_body:"+self.last_res_body
		print "tags"
		for i in self.tags:
			print i.decode("unicode-escape")

class Draw_graph_networkx(NiconicoMovie):
    def __init__(self, nico_string):
        super(Draw_graph_networkx, self).__init__(nico_string)

    def creating_nodes(self, G):
        #elist.append((1.0,3.0))
        for i in self.tags:
            G.add_edge(self.video_id, i)
        #G.add_edge(self.title, 4)

    def draw_graph_networkx(self, G):
        d=nx.degree(G)
        pos = nx.spring_layout(G)
        plt.figure(figsize = (15, 15))
        nx.draw_networkx_nodes(G, pos, nodelist=d.keys(), node_size=[v * 25 for v in d.values()], node_color = 'b',label=1)
        nx.draw_networkx_edges(G, pos, width = 1)
        nx.draw_networkx_labels(G, pos, font_size = 1, font_family = 'sans-serif', font_color = 'r')
        plt.savefig("niconico.png")

if __name__ == '__main__':
	#file_path = '/Users/suzukitoshiyuki/program/complexnetwork/data/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat'
    file_path = "C:\cygwin/files/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat/0000.dat"
    G = nx.Graph()
    f = open(file_path)
    line = f.readline().split("[")
    line_1 = line[0].split(",") + line[1].split(",")
    nico = Draw_graph_networkx(line_1)
    nico.creating_nodes(G)
    #nico.print_list()
    for i in xrange(60):
        line = f.readline().split("[")
        line_1 = line[0].split(",") + line[1].split(",")
        nico.__init__(line_1)
        nico.creating_nodes(G)

    nico.draw_graph_networkx(G)
    f.close()




	#print line[0].split(":")[1]
	#G = nx.cubical_graph()

	#plt.savefig("sample.png")