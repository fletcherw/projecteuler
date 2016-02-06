from math import ceil;
from math import sqrt;

def isPrime(p):
  if p < 2: return False
  if p % 2 == 0: return False
  for i in range(3,int(ceil(sqrt(p))), 2):
    if p % i == 0: return False
  return True

if __name__ == "__main__":
  longest = -20; 
  maxa = 0;
  maxb = 0;
  for a in range(-1000, 1000+1):
    for b in range(-1000, 1000+1):
      n = 0;
      while (isPrime(n * n + a * n + b)):
        n = n + 1
      n = n - 1;
      if n > longest:
        longest = n;
        maxa = a
        maxb = b
  print maxa * maxb
