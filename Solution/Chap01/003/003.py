import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(re.findall("[A-Za-z]", word)) for word in s.split(" ")])