import math;

squarefree = set();

def squareFree(n):
	if n % 4 == 0: return False;
	for k in range(3, int(n ** 0.5) + 1, 2):
		if n % (k ** 2) == 0: return False;
	return True;

tri = [[1]];
for n in range(1, 51):
	current = []
	for k in range (n + 1):
		val = 0;
		if (k == 0 or k == n): val = 1;
		else: val = (tri[n-1][k] + tri[n-1][k-1]);
		if (squareFree(val)): squarefree.add(val);
		current.append(val);
	tri.append(current);

tot = 0;

for n in squarefree:
	tot += n;
	
print tot;