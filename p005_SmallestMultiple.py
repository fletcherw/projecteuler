from math import log
factors = {2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}
for n in range(1, 20 + 1):
  for k in factors:
    if (n % k == 0):
      factors[k] = max(factors[k], int(log(n, k)))

num = 1
for k in factors: num *= pow(k, factors[k])
print num
