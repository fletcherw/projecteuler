def isPandigital(n):
  return sorted(str(n)) == map(str, range(1, len(str(n)) + 1))

def sieve(n):
  m = n + 1
  S = [True] * m
  S[0] = False
  S[1] = False
  
  pd_prime = None

  for i in range(2, m):
    if S[i]:
      for j in range(i+i, m, i):
        S[j] = False

  return S

if __name__ == "__main__":
  m_val = 0
  S = sieve(9999999)
  for i in range(1000, 9999):
    if S[i] and isPandigital(i):
      m_val = i

  for i in range(1000000, 9999999):
    if S[i] and isPandigital(i):
      m_val = i

print m_val
