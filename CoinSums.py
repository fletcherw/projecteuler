#coins = [1, 2, 5, 10, 20, 50, 100]
coins = [1, 2, 5]

count = 0 #for a 200 pence coin

def makeSum(goal, set):
	if goal
	if (len(set) == 1): return 1 if (goal % set[0] == 0) else 0
	ways = 0
	current = 0
	large = set[len(set) - 1]
	while current < goal:
		ways += makeSum(goal - current, set[:-1])
		current += large
	return ways

count += makeSum(10, coins)

print count
	
