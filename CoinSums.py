coins = [1, 2, 5, 10, 20, 50, 100]

count = 1 #for a 200 pence coin

def makeSum(goal, set):
	if (goal == 0): return 1
	if (len(set) == 1): return 1 if goal % (set[0]) == 0 else 0
	ways = 0
	for n in range(0, goal + 1, set.pop()):
		ways += makeSum(goal - n, set[:])	
	return ways

count += makeSum(200, list(coins))

print count
	
