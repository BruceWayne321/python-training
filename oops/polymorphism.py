
# polymorphism
'''
class manager:
	def role(self):
		print("i manage stuff")

class supervisor:
	def role(shewag,yg):
		shewag.hgh = yg
		print("i supervise ",shewag.hgh)


obj = supervisor()
obj.role("ds")
'''

#overloading
'''
class overloading:
	def role(self):
		print("hello")
	def role(self):
		print("world")
	def role(self):
		print("heheh")
obj = overloading()
obj.role()
'''

# overloading
'''
class overloading:
	def role(self):
		print("role 1")
	def role(self, name):
		self.name = name
		print("role 2", self.name)
	def role(self, name, city):
		self.name = name
		self.city = city
		print("role 3", self.name, self.city)

obj = overloading()
obj.role("bruce", "gotham") 
'''

# method overriding
'''
class parent:
	def study(self):
		print("study engineering")
	def car(self):
		print("no car")

class child(parent):
	def study(self):
		#super().study()
		print("become pilot")
obj = child()
obj.study()
obj.car()
'''