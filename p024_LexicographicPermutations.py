import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digitsout = ""

index = 999999 #the index of the permutation you're trying to calculate. Note that this is 0 indexed, so the 10th permutation would be 9, etc. etc.

for n in range(len(digits) - 1, -1, -1):
	fact = math.factorial(n)
	digitsout += str(digits.pop(int(math.floor(index/fact))))
	index = index % fact
	
print digitsout