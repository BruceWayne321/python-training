# single inheritance
'''
class parent:
	def __init__(self, name, branch, rollno):
		self.name = name
		self.branch = branch
		self.rollno = rollno
	def show(self):
		print(self.name, self.branch, self.rollno)


class child(parent):
	def showname(self):
		print("name is:", self.name)

obj = child()
obj.show()
obj.showname()
'''

# multilevel inheritance:
'''
class grandparent:
	def clgname(self, clg_name):
		self.clg_name = clg_name
	
class parent(grandparent):
	def dep(self, depname):
		self.depname = depname
		if self.depname.lower() == "cse":
			self.depid = 101
		else: self.depid = 0

class child(parent):
	def name(self):
		self.name = "Bruce"
	def show(self):
		print( "name is:", self.name)
		print("department name is:", self.depname)
		print("college name is:", "department id is:", self.depid)

obj = child()
obj.clgname("acpce")
obj.dep("cs")
obj.name()
obj.show()
'''

# multiple inheritance
'''
class parent1:
	def __init__(self, parent1name):
		self.parent1name= parent1name
	

class parent2:
	def __init__(self, parent2name):
		self.parent2name = parent2name

class child(parent1, parent2):
	def __init__(self, parent1name, parent2name):
		self.parent1name = parent1name
		self.parent2name = parent2name
		parent1.__init__(self,parent1name)
		parent2.__init__(self,parent2name)
	def show(self):
		print(self.parent1name, self.parent2name)


obj = child("martha", "james")
obj.show()
'''


















