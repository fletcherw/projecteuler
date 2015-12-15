f = file("p011_grid.txt")

grid = [map(int, l.split()) for l in f]

maxprod = 0;

for r in range(20-4):
  for c in range(20-4):
    # up-right
    if (r >= 3):
      prod = grid[r][c] * grid[r-1][c+1] * grid[r-2][c+2] * grid[r-3][c+3]
      if prod > maxprod: maxprod = prod;
    # right
    prod = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
    if prod > maxprod: maxprod = prod;
    # down-right
    prod = grid[r][c] * grid[r+1][c+1] * grid[r+2][c+2] * grid[r+3][c+3]
    if prod > maxprod: maxprod = prod;
    # down
    prod = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
    if prod > maxprod: maxprod = prod;
print maxprod
