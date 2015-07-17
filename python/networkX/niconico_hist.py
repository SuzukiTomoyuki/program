# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import string
from collections import Counter
import csv
import codecs
import json

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
        self.count_word = []

    def print_tags(self):
    	for i in self.tags:
    		print i.decode("unicode-escape") 

    def get_tags(self, tags_append):
    	for i in self.tags:
    		tags_append.append(i)


class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL

if __name__ == '__main__':
	file_path = '/Users/suzukitoshiyuki/program/complexnetwork/data/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat'
	# file_path = "C:\cygwin/files/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat/0000.dat"
	csvFile = codecs.open("./niconico.csv","w","shift_jis")
	writer = csv.writer(csvFile, CustomFormat())
	tags_append = []
	G = nx.Graph()
	f = open(file_path)
	nico = WordHistgram(f)
	for i in xrange(1000):
	    nico.__init__(f)
	    # nico.print_tags()
	    nico.get_tags(tags_append)

	counter = Counter(tags_append)
	counter_append = []
	for word, cnt in counter.most_common():
	    # print "%s %s" % (word.decode("unicode-escape"), cnt)
	    if cnt !=1 and word is not None :
	    	# print "%s,%s" % (word.decode("unicode-escape"), cnt)
	    	# writer.writerow((word.decode("unicode-escape"), cnt))
	    	row = ("%s->%s" % (word, cnt))
	    	print json.dumps(word)
    		writer.writerow(row)
	    	# counter_append.append("%s %s" % (word.decode("unicode-escape"), cnt))





