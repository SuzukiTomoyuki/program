# coding:utf-8 

class Item(object):
	def __init__(self,caption):
		self.caption = caption
	def makeList(self):
		pass

class Group(object):
	def __init__(self,group_name):
		self.group_name = group_name
		self.content = []
	def add(self,item):
		self.content.append(item)
	def output_file(self):
		self.filename = self.group_name+"組.txt"
		out = open(self.filename,"w")
		out.write(str(self.makeList()))
		out.close()
	def output_console(self):
		print self.makeList()
	def makeList(self):
		pass

class Name(Item):
	def __init__(self,name):
		super(Name,self).__init__(name)
		self.name = name

class Position(Item):
	def __init__(self,position):
		super(Position,self).__init__(position)
		self.position = position
		self.content = []
	def add(self,item):
		self.content.append(item)

class Factory(object):
	@classmethod
	def getFactory(cls,classname):
		module,kls = classname.rsplit(".",1)
		return getattr(__import__(module),kls)()
	def createGroup(self,group_name):
		pass
	def createName(self,name):
		pass
	def createPosition(self,position):
		pass