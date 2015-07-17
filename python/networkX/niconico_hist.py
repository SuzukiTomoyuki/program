# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import string

class NiconicoMovie(object):
	def __init__(self, f):
		line = f.readline().split("[")
		nico_string = line[0].split(",") + line[1].split(",")
		self.tags = []
		for i in nico_string[15:len(nico_string)]:
			if "tag" in i:
				self.tags.append(i.split(":")[1].translate(string.maketrans("", ""), "}]"))


class WordHistgram(NiconicoMovie):
    def __init__(self, f):
        super(WordHistgram, self).__init__(f)

    def print_tags(self):
    	for i in self.tags:
    		print i.decode("unicode-escape") 

if __name__ == '__main__':
	#file_path = '/Users/suzukitoshiyuki/program/complexnetwork/data/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat'
	file_path = "C:\cygwin/files/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat/0000.dat"
	G = nx.Graph()
	f = open(file_path)
	nico = WordHistgram(f)
	for i in xrange(50):
	    nico.__init__(f)
	    nico.print_tags()
