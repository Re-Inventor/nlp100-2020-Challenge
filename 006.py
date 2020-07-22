def get_ngram(l: list, n: int):
	return [l[i:i+n] for i in range(len(l)-n+1)]

sx = "paraparaparadise"
sy = "paragraph"
x = set(get_ngram(sx, 2))
y = set(get_ngram(sy, 2))

print("union:", x.union(y))
print("intersection:", x.intersection(y))
print("diff:", x.difference(y))

search = "se"

if search in x:
	print(search + " is in x")
else:
	print(earch + " isn't in x")
if search in y:
	print(search + " is in y")
else:
	print(search + " isn't in y")
