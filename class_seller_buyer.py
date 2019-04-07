class Person:
	'''Creation of the class Person'''
	def __init__(self, *arg):
		"""Initialise the person"""
		self.name = arg[0]
		self.lastname = arg[1]
		self.age = int(arg[2])
		print("(♯ {} has been created successfully.)".format(self.name))
class Goods:
	"""docstring for the Goods"""
	def __init__(self, *arg):
		self.goods_name = arg[0]
		self.caracteristics = arg[1]
		self.description = arg[2]
		self.quantity = int(arg[3])
		print("(♯ The goods: {} has been created successfully.)".format(self.goods_name))
	def buy(self):
		print("(→ You have bought: {:d} quantity of {}.)".format(self.quantity, self.goods_name))
	def sell(self):
		print("(→ You have sold: {:d} quantity of {}.".format(self.quantity, self.goods_name))
class Buyer(Person, Goods):
	"""Creation of the new person and new goods inside of our app."""
	def __init__(self, *arg):
		Person.__init__(self, arg[0], arg[1], arg[2])
		Goods.__init__(self, arg[3], arg[4], arg[5], arg[6])
		print("(♯ Buyer successfully created)")
	def buy(self):
		Goods.buy(self)
class Seller(Person, Goods):
	"""Creation of the new person and new goods inside of our app."""
	def __init__(self, *arg):
		Person.__init__(self, arg[0], arg[1], arg[2])
		Goods.__init__(self, arg[3], arg[4], arg[5], arg[6])
		print("(♯ Seller successfully created)")
	def sell(self):
		Goods.sell(self)
buyer = Buyer("Sendra", "Malala", 24, "Apple", "round and red", "This is a red and round apple from Antsirabe",10)
buyer.buy()