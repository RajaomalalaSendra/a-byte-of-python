class Person:
	'''Creation in general the person inside the population in general'''
	def __init__(self, *arg):
		'''Initialisation of the person'''
		self.name = arg[0]
		self.lastname = arg[1]
		self.birthday = arg[2]
		print("(↺ {} {} that has a birthday {} has been created)".format(self.name, self.lastname, self.birthday))
	def detail(self):
		'''The detail of this person'''
		print("(↺ This is {} {} who has been born on {}.)".format(self.name, self.lastname, self.birthday))
	def update(self):
		'''This is the simple way to modify that person'''
		print("Modification of that person:...")
		self.name = input("Update the name: ")
		self.lastname = input("Update the lastname: ")
		self.birthday = input("Update the birthday: ")
		print("Successfully update (↺ ⋆name {}⋆ ⋆lastname {}⋆ ⋆birthday {}⋆)".format(self.name, self.lastname, self.birthday))
class People(Person):
	'''Creation of the people in the '''
	counter = 0
	def __init__(self, *arg):
		'''Initialise that person inside the people'''
		Person.__init__(self, arg[0], arg[1], arg[2])
		self.diploma = arg[3]
		self.nationality = arg[4]
		print("(↺ And of the nationality {} and has the diploma {})".format(self.nationality, self.diploma))
		People.counter += 1
	def detail(self):
		'''The detail of this person of the people'''
		Person.detail(self)
		print("(↺ Nationality: {}, Diploma: {}.)".format(self.nationality, self.diploma))
	def delete(self):
		'''To delete that person inside the people'''
		print("(⌀ {} from {} has been delete.".format(self.name, self.nationality))
		People.counter -= 1
		if People.counter == 0:
			print("It is only {} the last people.".format(self.name))
		else:
			print("There are still {} people here.".format(People.counter))
	def update(self):
		'''To update all about the person inside that people'''
		Person.update(self)
		print("Now update the inside of the people class.")
		self.diploma = input("Update the diploma: ")
		self.nationality = input("Update the nationality: ")
		print("Successfully update (↺ ⋆diploma {}⋆ ⋆nationality {}⋆)".format(self.diploma, self.nationality))
	@classmethod
	def count(cls):
		print("All the people inside of your app is: {:d}".format(cls.counter))
class Governement(People):
	'''here is the people inside the governement worker'''
	count = 0
	def __init__(self, *arg):
		'''Initialise the worker of the governement.'''
		People.__init__(self, arg[0], arg[1], arg[2], arg[3], arg[4])
		self.governement_worker = arg[5]
		if self.governement_worker == True and arg[4] in ("malagasy", "Malagasy", "MALAGASY"):
			print("(↺ You are now successfully created to be member of the worker of the governement)")
			Governement.count += 1
		else:
			print("(⌀ You cannot be a worker inside the governement.)")
	def detail(self):
		'''The details of the worker as worker of the governement or not'''
		People.detail(self)
		if self.governement_worker == True:
			print("You are a member of the worker of the governement!!!!")
		else:
			print("You are not a member of the worker of the governement!!!!")
	def update(self):
		'''TO update the status of that person if it will be changed into worker of the governement'''
		People.update(self)
		self.governement_worker = input("Choose 'true' or 'false' for the worker of the governement: ")
		if self.governement_worker == 'true':
			self.governement_worker = True
			print("Update to be a worker of the governement.")
		elif self.governement_worker == 'false':
			self.governement_worker = False
			print("Update into the not a worker of the governement.")
		else:
			print("That is wrong command.")
	def delete(self):
		'''To delete that worker inside of that app.'''
		print("(⌀ {} from {} has been delete out of the worker of the governement.".format(self.name, self.nationality))
		Governement.count -= 1
		if Governement.count == 0:
			print("It is {} the last worker of the governement.".format(self.name))
		else:
			print("There are still {} workers inside the governement.".format(Governement.count))
	@classmethod
	def counter(cls):
		'''To count all the governement worker'''
		print("The Governement worker for now is: {}.".format(cls.count))
class Private(People):
	'''Here concerns about the private class of the person'''
	count = 0
	def __init__(self, *arg):
		'''To initialise the people to the private class.'''
		People.__init__(self, arg[0], arg[1], arg[2], arg[3], arg[4])
		self.sector = arg[5]
		self.position = arg[6]
		self.salary = int(arg[7])
		print("(↺ You are now successfully created to be member of the worker of the sector private.)")
		Private.count += 1
	def detail(self):
		'''The details of that person or people inside the private sector'''
		People.detail(self)
		print("(↺ Sector: {}, Position: {}, Salary: {}.)".format(self.sector, self.position, self.salary))
	def update(self):
		'''To update the people inside the private sector.'''
		People.update(self)
		self.sector = print("Update the sector: ")
		self.position = print("Update the position: ")
		self.salary = print("Update the salary: ")
		print("(↺ successfully update: ⋆sector {}⋆ ⋆position {}⋆ ⋆salary {}⋆)".format(self.sector, self.position, self.salary))
	def delete(self):
		"""To delete some member of the Private class"""
		print("(⌀ {} has been deleted successfully inside the private class app)".format(self.name))
		Private.count -= 1
	@classmethod
	def counter(cls):
		'''This is the best way to count all the member of the private class'''
		print("All the member of the private class for now is: {}".format(cls.count))
priv = Private("Malala", "Tiana", "10/11/1992", "Licence", "malagasy", "Agronomie", "Director of one big company", 1000000)
priv.detail()