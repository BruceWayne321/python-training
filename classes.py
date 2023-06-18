

class avgMarks:
	h = "hello"
	def __init__(self):
		self.name = "Bruce Wayne"
		self.city = "Gotham"
	def marks(self, math, phy, chem):
		self.math = math
		self.phy = phy
		self.chem = chem
		#return math+phy+chem
		#return math, phy, chem
		self.sum = math+phy+chem
	def avg(self):
		print(self.sum/3)
		print(self.name)
		print(self.h)
		#return a/3
	'''
	def avg(self, a):
		self.mark1, = a
	'''


obj = avgMarks()
#print(obj.marks())
#print(obj.avg(obj.marks(99,100,99)))
#obj.avg(obj.marks(99,100,99))
obj.marks(100,99,100)
obj.avg()


