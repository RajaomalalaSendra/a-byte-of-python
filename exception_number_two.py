true = True
try:
	while true:
		quit = ["q","quit", "exit"]
		text = input('Enter something --> ')
		if text in quit:
			exit = input("Do you want totally quit?(y/n) ")
			if exit == "y":
				true = False
		else:
			print('You entered {}'.format(text))
except EOFError:
	print('Why did you do an EOF on me?')
except KeyboardInterrupt:
	print('You cancelled the operation.')	