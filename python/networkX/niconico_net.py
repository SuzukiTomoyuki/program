# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import string

class NiconicoMovie:
	def __init__(self, nico_string):
		self.video_id = nico_string[0].split(":")[1]
		self.thread_id = nico_string[1].split(":")[1]
		self.title = nico_string[2].split(":")[1].decode("unicode-escape")
		self.description = nico_string[3].split(":")[1].decode("unicode-escape")
		self.thumbnail_url = nico_string[4].split(":")[1]
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

if __name__ == '__main__':
	file_path = '/Users/suzukitoshiyuki/program/complexnetwork/data/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat'

	f = open(file_path)
	line = f.readline().split("[")
	line_1 = line[0].split(",") + line[1].split(",")
	for x in line_1:
		#print x.split(":")[1].decode("unicode-escape")
		print x.decode("unicode-escape")
	nico = NiconicoMovie(line_1)

	f.close()



	#print line[0].split(":")[1]
	#G = nx.cubical_graph()

	#plt.savefig("sample.png")