import cal

class Sub(cal.Cal):
	def __init__(self,x,y):
		super(Sub,self).__init__("-",x,y)
	def cal_sub(self):
		self.answer = self.x-self.y
