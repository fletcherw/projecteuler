from math import sqrt

def is_abundant(x):
	sum = 1
	root = sqrt(x)
	for n in range(2, int(root) + 1, 1):
		if (x % n == 0): sum += n + x/n
	if (root == int(root)): sum -= root
	return sum > x

limit = 20161 + 1 #Actual lower limit for abundant sums is 20161
	
abundants = filter(is_abundant, range(12, limit, 1))

vals = range(limit)

for a in abundants:
	for b in abundants:
		if (a + b) >= limit: break
		if (b > a): break
		vals[a + b] = 0 #remove everything that is the sum of two abundants

print sum(vals) #sum everything else