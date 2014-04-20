import sets

abundants = sets.Set()

for x in range(12, 14062, 1):
	if (sum(filter(lambda f: x % f == 0, range(2, x, 1))) > x): abundants.add(x) #wheee functional programming

total = 0
	
for x in range(12, 28123, 1):
	if (len(sets.Set(map(lambda f: x - f, abundants)) & abundants) == 0): total += x

print total