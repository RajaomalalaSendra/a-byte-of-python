import time
try:
    with open("peee.txt") as f:
        for line in f:
            print(line,)
            time.sleep(2)
except IOError:
	print("That file doesn't exist.")