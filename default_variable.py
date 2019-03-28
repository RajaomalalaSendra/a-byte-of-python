# default variable inside of one function:
def functionality(var=1,var_two=3):
	print("this is the variable of ours inside of this: {} and {}".format(var, var_two))
try:
	var = int(input("enter that variable: "))
	var_two = int(input("enter the other variable: "))
except ValueError:
	print("that is not the good value!!")
except NameError:
	print("\n")
functionality(var,var_two)