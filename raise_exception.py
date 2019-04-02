class ShortInputException(Exception):
	'''A user-defined exception class.'''
	def __init__(self, length, atleast, atmost):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
		self.atmost = atmost
try:
	text = input('Enter something --> ')
	if len(text) < 3 and len(text) > 10:
		raise ShortInputException(len(text), 3, 10)
		# Other work can continue as usual here
except EOFError:
	print('Why did you do an EOF on me?')
except ShortInputException as ex:
	print ('ShortInputException: The input was {0} long, expected at least {1} and at most {2}.'\
	.format(ex.length, ex.atleast, ex.atmost))
else:
	print('No exception was raised.')