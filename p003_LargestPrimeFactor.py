def primeFactors(n):
  # requires n >= 1
  factors = [] 
  divisor = 2
  while (n > 1):
    if (n % divisor == 0):
      factors.append(divisor)
      n /= divisor
    else:
      if (divisor == 2): divisor = 3
      else: divisor += 2
  return factors

print primeFactors(600851475143)[-1]
