def cycle_len(n, d):
  m = {}
  i = 0
  while True:
    if n in m: return i - m[n]
    else: m[n] = i 

    if n == 0: return 0 
    if n >= d: 
      n %= d
    n *= 10
    i += 1

max_val = 0
max_i = 0
for i in xrange(1, 1000):
  val = cycle_len(1, i) 
  if (val > max_val):
    max_val = val
    max_i = i

print ""
print max_i 
