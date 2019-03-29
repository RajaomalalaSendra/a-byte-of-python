class Article:
	'''Creation of the new articles'''
	number_of_article = 0
	def __init__(self, name_article, nature, description):
		self.name_article = name_article
		self.nature = nature
		self.description = description
		print("That Article {} has been created.".format(self.name_article))
		Article.number_of_article += 1
	def delete(self):
		print("That Article {} has been successfully deleted.".format(self.name_article))
		Article.number_of_article -= 1
		if Article.number_of_article == 0:
			print('{} is the last articles inside of this app.'.format(self.name_article))
		else:
			print('There is still {:d} articles inside the app.'.format(Article.number_of_article))
	def modify(self):
		self.name_article = input("Modify the name of the article: ")
		self.nature = input("Modify the nature of the article: ")
		self.description = input("Modify the description of the article: ")
		print("That article {} has been successfully modify".format(self.name_article))
	def detail(self):
		print("The detail of the article:\n♯name : {}  \t♯nature : {}\n✗description : {}".format(\
			self.name_article, self.nature, self.description))
	@classmethod
	def has_many(cls):
		print("There are {} article disponible inside the app.".format(cls.number_of_article)) 
class User:
	'''Creation of the user'''
	user_number = 0
	def __init__(self, name_user, lastname_user, age_user, adress_user):
		'''Initialize the creation of the user'''
		self.name_user = name_user
		self.lastname_user = lastname_user
		self.age_user = int(age_user)
		self.adress_user = adress_user
		print("creation of the user {} with successful.".format(self.name_user))
		User.user_number += 1
	def delete(self):
		print("delete of the user {} with successful.".format(self.name_user))
		User.user_number -= 1
		if User.user_number == 0:
			print("The only user left has been before is : ✗{}.".format(self.name_user))
		else:
			print("THere is {} disponibles inside of this app.".format(User.user_number))
	def modify(self):
		'''A simple way of the modification of the user.'''
		print("You want to modify the admin: {}.".format(self.name_user))
		self.name_user = input("Modify your name: ")
		self.lastname_user = input("Modify your surname: ")
		self.age_user = input("Modify your age: ")
		self.adress_user = input("Modify your adress: ")
		try:
			print("In general the user new \nname : {} \tsurname : {}\nage : {:d}\tadress : {}".format(self.name_user,\
				self.lastname_user, int(self.age_user), self.adress_user))
			print("The admin has been successfully modify.")
		except ValueError:
			print("That is not allow because the age must be an integer or a number.")
	def detail(self):
		'''This is all the details about the user'''
		print('name : {}, surname : {}, age : {}.'.format(self.name_user, self.lastname_user, self.age_user))
	@classmethod
	def has_many(cls):
		print("There is {:d} user that is in this app for now.".format(User.user_number))
class Admin:
	"""docstring for Admin for real time and job"""
	number = 0
	def __init__(self, name, surname, age, adress, email):
		'''Initialize the admin and creation of the new admin.'''
		self.name = name
		self.surname = surname
		self.age = int(age)
		self.adress = adress
		self.email = email
		print('{} is the new admin inside of this app.'.format(self.name))
		Admin.number += 1
	def about(self):
		'''This is all about the admin'''
		print('name : {}, surname : {}, age : {}.'.format(self.name, self.surname, self.age))
	def modify(self):
		'''A simple way of the modification of the admin'''
		print("You want to modify the admin: {}.".format(self.name))
		self.name = input("Modify your name: ")
		self.surname = input("Modify your surname: ")
		self.age = input("Modify your age: ")
		self.adress = input("Modify your adress: ")
		self.email = input("Modify your email: ")
		try:
			print("In general the admin new \nname : {} \tsurname : {}\nage : {:d}\tadress : {}\temail : {}".format(self.name\
				, self.surname, int(self.age), self.adress, self.email))
			print("The admin has been successfully modify.")
		except ValueError:
			print("That is not allow because the age must be an integer or a number.")
	def delete(self):
		'''To delete the admin'''
		print('The {} is gonna be deleted inside of the app.'.format(self.name))
		Admin.number -= 1
		if Admin.number == 0:
			print('{} is the last admin inside of this app.'.format(self.name))
		else:
			print('There is still {:d}  admin members.'.format(Admin.number))
	@classmethod
	def has_many(cls):
		print("There is {:d} admin that is in this app for now.".format(Admin.number))

admin1 = Admin("sendra", "sendara", 45, "Here in Tana", 'sendra@malala.com')
admin2 = Admin("malala", "malala1", 30, "Here in Tana too", 'malala@malala.com')
Admin.has_many()
admin1.modify()
admin1.delete()