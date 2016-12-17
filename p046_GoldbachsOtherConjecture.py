import math

def sieve(n):
  m = n + 1
  out = []
  S = [True] * m
  S[0] = False
  S[1] = False
  
  pd_prime = None

  for i in range(2, m):
    if S[i]:
      out.append(i)
      for j in range(i+i, m, i):
        S[j] = False

  return S, out 

def odds():
  n = 3
  while True:
    yield n
    n += 2

S, primes = sieve(100000)
series = odds()

for n in series:
  if S[n]: continue 
  done = False
  for p in primes:  
    if p > n: break
    i = math.sqrt((n - p) / 2)
    if math.fabs(i - math.ceil(i)) < 0.000001:
      done = True
      break
  if not done:
    print n
    break
