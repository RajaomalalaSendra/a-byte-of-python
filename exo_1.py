# printing all the different format in python
my_name = "Sendra"
print("my name is {}".format(my_name))
# printing the number
print('{0:_^11}'.format('hello'))
print('{0:_^10}'.format('init'))
# printing the float value of the number
print('{0:.3f}'.format(1.0/3))
def the_variable(var):
	try:
		var = float(var)
		if var >= 0:
			print('{0:.3f}'.format(var/4))
		else:
			print("This number is really negative")
	except ValueError:
		print("there is an error that occur here.")
var = input("the number please: ")
the_variable(var)