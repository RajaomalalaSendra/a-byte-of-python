class PersonHere:
	'''To create the person in general.'''
	def __init__(self, name, lastname, age):
		self.name = name
		self.lastname = lastname
		self.age = int(age)
		print('({} has been created)'.format(self.name))
	def detail(self):
		'''To get the detail about that person.'''
		print('(⭒name⭒: {}, ⭒lastname⭒: {}, ⭒age⭒: {:d})'.format(self.name, self.lastname, self.age))
	def modify(self):
		self.name = input("Modify the name: ")
		self.lastname = input("Modify the lastname: ")
		self.age = input("Modify the age: ")
class SaynaStudent(PersonHere):
	'''To get the person who study at sayna.'''
	number_student = 0
	def __init__(self, name, lastname, age, course, duration, finalproject):
		PersonHere.__init__(self, name, lastname, age)
		self.course = course
		self.duration = duration
		self.finalproject = finalproject
		print("{} who attend the {} has been created.".format(self.name, self.course))
		SaynaStudent.number_student += 1
	def detail(self):
		'''This is the detail about that student in sayna.'''
		PersonHere.detail(self)
		print("This student is called : {} and he/she study at Sayna during {} \nand his/her final project concern about the {}".format(\
			self.name, self.duration, self.finalproject))
	def modify(self):
		'''To make an update about the sayna staff'''
		print("Modification of the student inside of sayna student.")
		PersonHere.modify(self)
		self.course = input("Modify the course: ")
		self.duration = input("Modify the duration: ")
		self.finalproject = input("Modify the final project: ")
		try:
			print("Modify successfully!!")
			print("(name: {})(lastname: {})(age: {:d})(course: {})(final project: {})".format(self.name, \
				self.lastname, int(self.age), self.course, self.finalproject))
		except ValueError:
			print("Very sorry for that problem. We gonna fix it as soon as possible!!!")
	def delete(self):
		'''This is the method to delete some student in sayna when they not attend anymore the study'''
		print("You have successfully delete {} inside that app of Sayna Student.".format(self.name))
		SaynaStudent.number_student -= 1
		if SaynaStudent.number_student == 0:
			print("{} has been the last student attend sayna.".format(self.name))
		else:
			print("There are still {} who attend the sayna course.")
	@classmethod
	def all_student(cls):
		'''To know the number of the student inside of all of the sayna etablissement.'''
		print("All the student in sayna are {:d}.".format(cls.number_student))
class SaynaStaff(PersonHere):
	'''This is all about the staff here in the sayna.'''
	number_staff = 0
	def __init__(self, name, lastname, age, position, salary):
		PersonHere.__init__(self, name, lastname, age)
		self.position = position
		self.salary = int(salary)
		print("Welcome  to Sayna Staff {}!!!".format(self.name))
		SaynaStaff.number_staff += 1
	def detail(self):
		'''To know all the detail about the staff here in sayna.'''
		PersonHere.detail(self)
		print("He/She is the responsible of: {} and get the salary of {:d} Ariary every month.".format(self.position, self.salary))
	def modify(self):
		'''To make an update about the sayna staff'''
		print("Modification of the student inside of sayna staff.")
		PersonHere.modify(self)
		self.position = input("Modify the position: ")
		self.salary = input("Modify the salary: ")
		try:
			print("Modify successfully!!")
			print("(name: {})(lastname: {})(age: {:d})(position: {})(salary: {:d})".format(self.name, \
				self.lastname, int(self.age), self.position, int(self.salary)))
		except ValueError:
			print("Very sorry for that problem. We gonna fix it as soon as possible!!!")
	def delete(self):
		'''To delete one of the staff here in sayna.'''
		print("{} has been totally take away from sayna.".format(self.name))
		SaynaStaff.number_staff -= 1
		if SaynaStaff.number_staff == 0:
			print("I think {} is the last staff inside Sayna.".format(self.name))
		else:
			print("There are still {:d} persons that work inside Sayna.".format(SaynaStaff.number_staff))
	@classmethod
	def all_staff(cls):
		'''To show all the staff inside the sayna for all of these situations.'''
		if cls.number_staff < 10:
			print("Sayna has a staff less than 10 persons.")
		else:
			print("Sayna has a staff more than 10. Exactly {} persons.".format(cls.number_staff))
class SaynaAlternance(PersonHere):
	'''This is the detail about the people who have attend Sayna but now inside of the sayna alternance.'''
	number_alternance = 0
	def __init__(self, name, lastname, age, entreprise, salary, speciality):
		'''initialize the new person that enter into the alternance
		...
		'''
		PersonHere.__init__(self, name, lastname, age)
		self.entreprise = entreprise
		self.salary = int(salary)
		self.speciality = speciality
		print("Welcome  to Sayna Alternance Guy. Nice to meet you {}!!!".format(self.name))
		SaynaAlternance.number_alternance += 1
	def detail(self):
		'''To know all the detail about the alternance student here in sayna.'''
		PersonHere.detail(self)
		print("He/She works at : {} and get the salary of {:d} Ariary every month.\nThe speciality is {} languages.".format(self.entreprise, self.salary, self.speciality)) 
	def modify(self):
		'''To make an update about the sayna in alternance'''
		print("Modification of the student inside of sayna alaternance.")
		self.name = input("Modify the name: ")
		self.lastname = input("Modify the lastname: ")
		self.age = input("Modify the age: ")
		self.entreprise = input("Modify the entreprise: ")
		self.salary = input("Modify the salary: ")
		self.speciality = input("Modify the speciality: ")
		try:
			print("Modify successfully!!")
			print("(name: {})(lastname: {})(age: {:d})(entreprise: {})(salary: {:d})".format(self.name, \
				self.lastname, int(self.age), self.entreprise, int(self.salary)))
		except ValueError:
			print("There is some error here!! We are very sorry for that!! We gonna fix it as soon as possible!!!")
	def delete(self):
		'''To delete one of the alternance student here in sayna.'''
		print("{} has been totally take away from alternance of sayna.".format(self.name))
		SaynaAlternance.number_alternance -= 1
		if SaynaAlternance.number_alternance == 0:
			print("I think {} is the last alternance inside Sayna.".format(self.name))
		else:
			print("There is/are still {:d} alternant student inside Sayna.".format(SaynaAlternance.number_alternance))
	@classmethod
	def all_alternants(cls):
		'''The number of all alternants inside Sayna for the real time and so on...'''
		if cls.number_alternance < 10:
			print("Sayna has an alternants less than 10 persons.")
		else:
			print("Sayna has an altenants more than 10. Exactly {} persons.".format(cls.number_alternance))


sendra = SaynaAlternance("sendra", "malala", 34, "entreprise 1", 200000, "back end")
malala = SaynaStudent("malala", "sendra", 34, "THP", "3 months", "About the school")
matina = SaynaStaff("matina", "razafimahefa", 21, "CEO", 120000)
sendra.modify()