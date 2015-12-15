size = 1000000
goal = 10001
sieve = [True] * size

cur = 2 
numprimes = 1
while (cur < size and numprimes < goal):
  for n in range(0, size, cur):
    sieve[n] = False
  cur += 1
  while (cur < size and not sieve[cur]): cur += 1
  numprimes += 1

print cur
