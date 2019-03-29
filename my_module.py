# this the module that I have created for today
if __name__ == "__main__":
	print("We are still at my module.")
else:
	print("My module has been imported successfully.")
def useful_function(*arg):
	'''To print the list of arguments inside of that function:
	The useful_function has a tuple of arguments.
	Example:
	useful_function(1,3,3)
	...
	all the arg is : (1,3,3)
	the arg number 1  is : 1
	the arg number 2  is : 3
	the arg number 3  is : 3
	'''
	print("all the arg is : {}".format(arg))
	for a in range(0,len(arg)):
		print("the arg number {} is : {}".format(a+1,arg[a]))
__version__ = "0.0.1.1"