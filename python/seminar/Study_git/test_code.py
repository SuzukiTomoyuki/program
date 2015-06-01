import unittest

class TestFunctions(unittest.TestCase):
	def setUp(self):
		print "start test"
	def test_add(self):
		print "\ntest add module"
		import add
		a = add.Add(1,5)
		a.cal_add()
	def test_sub(self):
		print "\ntest sub module"
		import sub
		a = sub.Sub(5,2)
		a.cal_sub()
	def test_multi(self):
		print "\ntest multi module"
		import multi
		a = multi.Multi(3,1)
		a.cal_multi()
	def test_div(self):
		print "\ntest div module"
		import div
		a = div.Div(3,2)
		a.cal_div()

if __name__ == '__main__':
	unittest.main()