def cipher(s: str):
	return "".join([chr(219-ord(ch)) if ch.islower() else ch for ch in s])

s = "1aA2bB3cC4dD"
print(cipher(s))
print(cipher(cipher(s)))
