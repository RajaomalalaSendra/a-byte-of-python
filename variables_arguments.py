# There are two things we gonna do here for the creation of the variable
def functional(*numbers):
	print(numbers)
	for i in numbers:
		print("*" * 10)
		print(i)
		print("*" * 10)
def functional_two(**numbers):
	print(numbers)
	count = 0
	for i in numbers:
		print("*" * 10)
		print(numbers)
		print("*" * 10)
functional(4,5,3,2,4)
functional_two(initial=0,a=2,b=2,c=12)
nat = {'me': 34, 'notme': 45}
functional_two(nat=nat)
# using the pass statement
def stat():
	pass
stat()
# using of the return inside of one function
def some_function(*number_one):
	number,number_2 = number_one[0],number_one[1]
	if number > number_2:
		return "the number is greater than the number_2"
	elif number < number_2:
		return "the number is less than the number_2"
	else:
		return "the two number has the same value"

print(some_function(3,5))