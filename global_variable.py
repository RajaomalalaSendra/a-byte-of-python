# creating a global variable in python
def globalize():
	global variable
	variable = input("enter the global variable from here: ")
globalize()
print("Here is the variable you have just enter: {}".format(variable))