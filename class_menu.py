class Menu:
	def __init__(self, *arg):
		self.menu = arg[0]
		self.detail = arg[1]
		self.quit = arg[2]
		self.show_letter = arg[3]
		self.show_number = arg[4]
		self.contact = arg[5]
		self.adress = arg[6]
	def menu(self):

	def detail(self):

menu = Menu('menu', )
while True:
	menu = int(input("Choose 1.Menu 2.Detail 3.Quit: "))
	if menu == 1:
				