from math import factorial

# https://oeis.org/A000984
grid_size = 20
paths = factorial(2*grid_size)//factorial(grid_size)**2
print(paths)
