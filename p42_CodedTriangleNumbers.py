tris = set()
for n in range(1, 30, 1): tris.add(n * (n + 1) / 2)

words = file("p42_words.txt").next().split(",")
words = map(lambda s: s[1:-1], words) #trim the quotes

count = 0

def digitval(char): return ord(char) - ord('A') + 1

for str in words:
	sum = 0
	for char in str: sum += digitval(char)
	if sum in tris: count += 1

print count
