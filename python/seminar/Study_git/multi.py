import cal

class Multi(cal.Cal):
	def __init__(self,x,y):
		super(Multi,self).__init__("*",x,y)
	def cal_multi(self):
		self.answer = self.x*self.y