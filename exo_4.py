# conting the length of each word.
while True:
	a = input("enter something here: ")
	if a == "quit":
		print("move to the other menu and really quit!!")
		break
	elif a == "done":
		print("You have done what you have just created.")
		break
	else:
		print("the length of the things you have write is: {}".format(len(a)))
# getting all the word inside the sentence
while True:
	sentence = input("Enter one or more sentences or enter \"quit\" to quit: ")
	if sentence == "quit":
		print("you quit that menu!!!")
		break
	else:
		sentence = sentence.split(' ')
		print("Here is the list of all the words inside that sentence: {}".format(sentence))
# getting all the sentence that the user have write
while True:
	print("another menu")
	sentence = input("Enter one or more sentences or enter \"quit\" to quit: ")
	if sentence == "quit":
		print("you quit that menu!!!")
		break
	else:
		sentence = sentence.split(".")
		if sentence[:-1]=='':
			print("Your all sentences is here: {}".format(sentence))