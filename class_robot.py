class Robot:
	"""Represents a robot, with a name."""
	# A class variable, counting the number of robots
	population = 0
	def __init__(self, name):
		"""Initializes the data."""
		self.name = name
		print("(Initializing {})".format(self.name))
		# When this person is created, the robot
		# adds to the population
		Robot.population += 1
	def die(self):
		"""I am dying."""
		print("{} is being destroyed!".format(self.name))
		Robot.population -= 1
		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(Robot.population))
	def say_hi(self):
		"""Greeting by the robot.
		Yeah, they can do that."""
		print("Greetings, my masters call me {}.".format(self.name))
	@classmethod
	def how_many(cls):
		"""Prints the current population."""
		print("We have {:d} robots.".format(cls.population))
# the new robot created
droid1 = Robot("R2-D2")
# the robot is greeting
droid1.say_hi()
# count all the robot
Robot.how_many()
# create the second robot
droid2 = Robot("C-3PO")
# the second robot is greeting
droid2.say_hi()
# count all the robot
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
# Kill the two robots
droid1.die()
print("*"*10)
droid1.say_hi()
print("*"*10)
droid2.die()
# Count all the robot inside the Robot class
Robot.how_many()
droid3 = Robot("DR. ROBO")
droid3.say_hi()
Robot.how_many()
class Input:
	'''To get the input from the user.'''
	user_count = 0
	def __init__(self, name, surname,age):
		self.name = name
		self.surname = surname
		self.age = int(age)
		print("User {} has been created.".format(self.name))
		Input.user_count += 1
	def change(self):
		self.name = input("You want to change your name: ")
		self.surname = input("You want to change your surname: ")
		self.age = input("You want to change your age: ")
		try:
			print("Your statut has been successfully change.\nAs: {} {} is  {:d} years old.".format(self.name, self.surname, int(self.age)))
		except ValueError:
			print("Not that because age is an integer.")
	def delete(self):
		print("The user {} {} has been deleted.".format(self.name, self.surname))
		Input.user_count -= 1
		if Input.user_count == 0:
			print("{} is the only last user here.".format(self.name))
		else:
			print("There is still {:d} users inside of this apps.".format(Input.user_count))
	@classmethod
	def how_many(cls):
		'''Print all the count of all the current user.'''
		print("We have {:d} users inside of the app in general.".format(cls.user_count))
user = Input("sendra", "Rajaomalala", 45)
user.change()
Input.how_many()
user2 = Input("Nomena", 'Nantenaina', 40)
user2.change()
Input.how_many()
user.delete()
Input.how_many()