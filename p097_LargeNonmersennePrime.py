# Project Euler Problem 97

product = 1;

for i in range(7830457):
    product *= 2
    product %= 100000000000

product *= 28433

product += 1

print(str(product)[-10:])
