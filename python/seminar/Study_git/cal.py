class Cal(object):
	def __init__(self,cal_key,x,y):
		self.answer = 0
		self.cal_key = cal_key
		self.x = x
		self.y = y
	def print_answer(self):
		print str(self.x)+self.cal_key+str(self.y)+"="+str(self.answer)
		