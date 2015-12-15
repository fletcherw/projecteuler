from operator import mul
print sum(map(int, str(reduce(mul, range(1, 101), 1))))
