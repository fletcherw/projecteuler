# brute force. Non-elegant, but it works

def isPalindrome(n): s = str(n); return s == s[::-1]

highest = -1;

for i in range(100, 1000):
  for j in range(i, 1000):
    num = i * j
    if (isPalindrome(num)):
      if (num > highest): highest = num 

print highest
