def get_ngram(l: list, n: int):
	return [l[i:i+n] for i in range(len(l)-n+1)]

s = "I am an NLPer"
print(get_ngram(s.split(" "), 2))
print(get_ngram(s, 2))