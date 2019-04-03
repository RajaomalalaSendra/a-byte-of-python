import re

pattern = 'text'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))

pattern_two = 'sendra'
text_two = 'this is rajaomalala sendra andriampanjato. sendra is my coworker.'

match_two = re.search(pattern_two, text_two)

a = match_two.start()
b = match_two.end()

print("I've found '{}' in the '{}'\nfrom  {} to {} ('{}')".format(
	match_two.re.pattern, match_two.string, a, b, text_two[a:b]))