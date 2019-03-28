import random
def guess_number(number):
	randomize = random.randint(1,number)
	truth = True
	while truth:
		try:
			get_number_from_user =  int(input("Guess the rigth number between 1 and {} ".format(number)))
			if get_number_from_user < randomize:
				print("this number is more little than the guess number")
			elif get_number_from_user > randomize:
				print("it is greater than the guess number")
			else:
				truth = False
		except ValueError:
			print("You need to try the number as it is said.")
	print("You win and that is the end of the game for today.")
def the_levels(that_level):
	print("That is the level for the number between 1 and {}".format(that_level))
def level():
	levels = [10, 100, 1000, 10000, 100000, 1000000]
	get = True
	while get:
		level = int(input("Choose the level you want to do: 1. 2. 3. 4. or 5. or 0 to quit "))
		try:
			if level == 1:
				the_levels(levels[0])
				guess_number(levels[0])
			elif level == 2:
				the_levels(levels[1])
				guess_number(levels[1])
			elif level == 3:
				the_levels(levels[2])
				guess_number(levels[2])
			elif level == 4:
				the_levels(levels[3])
				guess_number(levels[3])
			elif level == 5:
				the_levels(levels[4])
				guess_number(levels[4])
			elif level == 0:
				print("You've successfully quit that program.")
				get = False
			else:
				print("Try again to enter another time that number.")
		except ValueError:
			print("The program don't like this.")
level()