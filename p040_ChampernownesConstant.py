indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
vals = ""
for n in range(1, 190000): #upper bound by trial + error
	vals += str(n)

print reduce(lambda a, b: a * b, map(lambda f: int(vals[f - 1]), indexes)) #map returns a list of the integers at the various indexes within our huge string, then reduce multiplies them all together