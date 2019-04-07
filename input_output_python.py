class Palindrome:
	def __init__(self, text):
		self.text = text
		print("({} is created)".format(self.text))
	def reverse(self):
		return self.text[::-1]
	def is_palindrome(self):
		return self.text == self.text[::-1]

something = input("Enter text: ")
pal = Palindrome(something)
if pal.is_palindrome():
	print("Yes, it is a palindrome")
else:
	print("No, it is not a palindrome")