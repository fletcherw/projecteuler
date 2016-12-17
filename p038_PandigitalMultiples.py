m_val = 0

def construct(n, m):
  l = map(lambda v : v * n, range(1, m+1))
  return ''.join(map(str, l))

def is_pandigital(n):
  return sorted(n) == list("123456789")

for n in xrange(1, 10000):
  for m in xrange(2, 9):
    num = construct(n, m) 
    if is_pandigital(num):
      v = int(num)
      if v > m_val:
        m_val = v
    if len(num) > 9: break

print m_val
