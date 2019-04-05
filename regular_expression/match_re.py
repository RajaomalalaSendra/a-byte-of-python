import re

# Precompile the patterns
word = input("enter one or more words in this app: ")
regexes = [
    re.compile(p)
    for p in word.split(" ")
]
lister = set()

try:
	with open('genesisy.txt') as text:
		for t in text:
			lister.add(t)
except IOError:
	print("Cannot import that text.")
text = " ".join(lister)
for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')
    if regex.search(text):
        print('it is really a malagasy word!')
    else:
        print('it is not a malagasy word!')