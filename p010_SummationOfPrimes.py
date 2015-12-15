size = 2000000
sieve = [True] * size
sieve[0] = False
sieve[1] = False

cur = 2 
total = 2;
while (cur < size):
  for n in range(cur, size, cur):
    sieve[n] = False
  cur += 1
  while (cur < size and not sieve[cur]): cur += 1
  if (cur < size): total += cur

print total
