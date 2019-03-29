# this the simple function and program in python for creating and get the word in malagasy:
import nltk
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
	the_text = input("enter the name of the file in txt: ")
	try:
		f = open(the_text, "w")
	except:
		print("The file already exist.")
	file = file.split(" ")
	get_verb_and_noun = set()
	mylist = list()
	for word in file:
		if word[:1] == "n" or word[:1] == "m" or word[:1] == "h" or word[:1] == "f":
			get_verb_and_noun.add(word)
	text = " ".join(sorted(get_verb_and_noun))
	last_text = nltk.tokenize.regexp_tokenize(text, pattern=r'\s+', gaps=True)
	f.write(" ".join(last_text))
	f.close()
def get_all():
	while True:
		file_path = input("enter the name of the path you want to get: ")
		file = getter(file_path)
		get_verb_and_noun(file)
		q = input("It is finished, do you want to quit (q) or do another extraction of the text: ")
		if q in ('q','Q','quit', 'Quit', 'QUIT'):
			print("see you next time!!!")
			break
if __name__ == "__main__":
	print("You are inside the module tenymalagasy")
else:
	print("Successfully import the tenymalagasy module.")