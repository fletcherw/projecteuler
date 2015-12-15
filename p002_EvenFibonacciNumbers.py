current = 1 
prev = 0
total = 0
while (current < 4000000):
  if (current % 2 == 0): total += current
  current = current + prev
  prev = current - prev
print total
