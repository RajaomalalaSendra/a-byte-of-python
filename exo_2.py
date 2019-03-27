def enter():
	global x,y
	x = input("enter a number: ")
	y = input("enter a string: ")

def multiply(number,string):
	try:
		if int(string) == True:
			print(int(string) * int(number))
		else:
			print(string * int(number))

	except TypeError and ValueError:
		print("I mean you cannot do that operation.")
enter()
multiply(x,y)