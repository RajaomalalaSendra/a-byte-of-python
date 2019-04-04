import re

# Precompile the patterns
word = input("enter one or more words in this app: ")
regexes = [
    re.compile(p)
    for p in word.split(" ")
]
lister = list()

try:
	with open('text.txt') as text:
		for t in text:
			lister.append(t)
except IOError:
	print("Cannot import that text.")
text = " ".join(lister)

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')