# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pylab as plt
from numpy.random import *
import string
from collections import Counter
import csv
import codecs
import json
import glob

class NiconicoMovie(object):
	def __init__(self, f):
		self.line = f.readline()
		line_temp = self.line.split("[")
		try:
			nico_string = line_temp[0].split(",") + line_temp[1].split(",")
			self.tags = []
			for i in nico_string[15:len(nico_string)]:
				if "tag" in i:
					self.tags.append(i.split(":")[1].translate(string.maketrans("", ""), "}]"))
		except:
			pass


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
	# file_path = '/Users/suzukitoshiyuki/program/complexnetwork/data/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat'
	csvFile = codecs.open("./niconico.csv","w","utf-8")
	tags_append = []
	tags_append2 = []
	count = 0
	path = "C:\cygwin/files/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat/"
	for file in glob.glob(path + "*.dat"):
		# print file
		# file_path = "C:\cygwin/files/tcserv.nii.ac.jp/access/dxfsrs1004@gmail.com/2790ed0df755cd51/nicocomm/data/video/0000.dat/0000.dat"
	
		f = open(file)
		nico = WordHistgram(f)
		while nico.line:
		    nico.__init__(f)
		    # nico.print_tags()
		    if count < 500:
		    	nico.get_tags(tags_append)
		    else:
		    	break
		count+=1

	counter = Counter(tags_append)
	for word, cnt in counter.most_common():
	    # print "%s %s" % (word.decode("unicode-escape"), cnt)
	    if cnt > 9:
	    	# print "%s,%s" % (word.decode("unicode-escape"), cnt)
	    	# writer.writerow((word.decode("unicode-escape"), cnt))
	    	print >> csvFile, json.loads(json.dumps(word)).decode("unicode-escape"),u" "+str(cnt)

	f.close()





