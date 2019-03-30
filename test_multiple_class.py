class One:
	def __init__(self, one):
		self.one = one
	def delete(self):
		print("This is the delete of the one.")
class Two:
	def __init__(self, two):
		self.two = two
	def detail(self):
		print("This is just the detail about the two")
class Four:
	def __init__(self, four):
		self.four = four
	def detail(self):
		print("This is just the detail about the four")
class Five:
	def __init__(self, five):
		self.five = five
	def detail(self):
		print("This is just the detail about the five")
class Three(One, Two, Four, Five):
	def __init__(self, one, two, four, five):
		One.__init__(self, one)
		Two.__init__(self, two)
		Four.__init__(self, four)
		Five.__init__(self, five)
		print("({} {} {} {})".format(self.one, self.two, self.five, self.four))
	def mixture(self):
		One.delete(self)
		Two.detail(self)
		Five.detail(self)
		Four.detail(self)
three = Three("me", "and you", "we", "and them")
three.mixture()