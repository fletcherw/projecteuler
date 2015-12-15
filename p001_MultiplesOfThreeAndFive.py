def isMult(n): return ((n % 3 == 0) or (n % 5 == 0))
print sum(filter(isMult, range(1, 1000))) 
