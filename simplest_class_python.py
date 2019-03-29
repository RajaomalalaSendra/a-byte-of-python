class Person():
	"""This is the class Person"""
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def head(self):
		print("This is the head!!!")
	def add(self):
		print("The result is: ", self.x + self.y)
	def substraction(self):
		print("The result is: ", self.x - self.y)
	def multiplication(self):
		print("The result is: ", self.x * self.y)
	def division(self):
		print("The result is: ", self.x / self.y)
p = Person(3,4)
p.head()	
p.add()
p.substraction()
p.multiplication()
p.division()	