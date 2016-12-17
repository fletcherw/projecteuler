import math

def pentagonal():
  n = 166 
  while True:
    yield n * (3 * n - 1) / 2
    n += 1

def isHexagonal(x):
  i = math.sqrt(8 * x + 1)
  return (math.fabs(i - math.floor(i)) < 0.000001) \
         and int(i) % 4 == 3

n = 165 * (3 * 165 - 1) / 2 
assert isHexagonal(n)

p = pentagonal()

for n in p:
  if isHexagonal(n):
    print n
    break
