factors = [13, 11, 7, 5, 3, 2]

nums = map(str, range(17, 1000, 17))

def notrepeats(item): 
	for n in map(str, range(10)):
		if item.count(n) > 1:
			return False
	return True
	
def divisible(x, num): return int(num[:3]) % x == 0
	
nums = filter(notrepeats, nums) 							 #takes out the repeats
nums = map(lambda item: '0' * (3 - len(item)) + item, nums) #pads the numbers that have fewer than 3 digits with 0

for val in factors:
	nums = sum(map(lambda n: map(lambda k: str(n) + k, nums), range(10)), []) #get all combinations for the current valid numbers and the digits 0-9 i.e [213, 417] -> [0213, 1213, 2213, ... , 9213, 0417, 1417, ... , 9417]
	nums = filter(notrepeats, nums) 											#filter out the values that repeat digits
	nums = filter(lambda k: divisible(val, k), nums)							#filter out the values that aren't divisible by the requisite factor (val)
	
nums = map(lambda x: str(filter(lambda k: x.count(str(k)) == 0, range(0, 10))[0]) +  x, nums) #figures out whichever digit is missing from the 9 digit number and prepends it
nums = map(int, nums)																			#convert all of the strings to ints

print sum(nums)
		