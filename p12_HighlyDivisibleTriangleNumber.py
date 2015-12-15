from collections import defaultdict

def numDivisors(n):
  # requires n >= 1
  factors = defaultdict(int)
  divisor = 2
  while (n > 1):
    if (n % divisor == 0):
      factors[divisor] += 1
      n /= divisor
    else:
      if (divisor == 2): divisor = 3
      else: divisor += 2
  numDivisors = 1
  for (k, v) in factors.items():
    numDivisors *= (v+1)
  return numDivisors

def findNumber():
  index = 1
  number = 1
  while (numDivisors(number) <= 500):
    index += 1
    number += index
  print number

findNumber()
