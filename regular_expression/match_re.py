import re

# Precompile the patterns
word = input("enter one or more words in this app: ")
regexes = [
    re.compile(p)
    for p in word.split(" ")
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')