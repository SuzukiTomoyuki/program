class Factory(object):
	@classmethod
	def getFacrtory(cls,classname):
		module,kls = classname.rplit(".",1)
		return getattr(__import__(module),kls)()