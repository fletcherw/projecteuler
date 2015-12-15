index = 2
length = 1;
mag = 10;
current = 2
prev = 1
while (length < 1000):
  current = current + prev
  prev = current - prev
  index += 1
  if (current > mag):
    mag *= 10
    length += 1
print index + 1 # index was last with length < 1000
