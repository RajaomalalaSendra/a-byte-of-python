# User error handler
class Error(Exception):
	'''This is a great error for this apps.'''
	pass

def division():
	while True:
		first = input("enter a number inside of this apps: ")
		second = input("enter the second number: ")
		try:
			first = int(first)
			second = int(second)
			div = first/second
			print('{0:.3f}'.format(div))
			break

		except ValueError:
   			print("there is a error in the value.")

		except (TypeError, ZeroDivisionError):
			print("this number is zero not supported.")

		except:
   			print("We need to consider that there is another error inside of it.")
def there_is():
	there = input("Enter one variable: ")
	try:
		there = int(there)
		print(there)
	except ValueError:
		print('...')
division()
there_is()