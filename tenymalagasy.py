# this the simple function and program in python for creating and get the word in malagasy:
def getter(file):
	'''The getter(file) function is used to get the file.
	The second usage is to make quick the creation of the exportation of the file.
	...
	file: This is the argument that concern the path that contain the file.
	'''
	try:
		file = open(file).read()
		return file
	except FileNotFoundError:
		print("That file doesn't exist.")
file = getter("/home/malala/Desktop/Genesisy1.txt")
def get_verb_and_noun(file):
	'''The get_verb_and_noun function is used to get the verb and the noun in Malagasy.
	We can use it for the specific one.
	...
	For example:
	The 'manana' is the present.
	The 'hanana' is the future.
	The 'nanana' is the past simple.
	The 'fananana' is the noun.
	The 'anana' is the root.
	'''
	file = file.split(" ")
	get_verb_and_noun = set()
	for word in file:
		if word[:1] == "n" or word[:1] == "m" or word[:1] == "h" or word[:1] == "f":
			get_verb_and_noun.add(word)
	print(get_verb_and_noun)
get_verb_and_noun(file)