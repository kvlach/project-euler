#!/usr/bin/env python3

def special_pythagorean_triplet():
  result = []
  for a in range(0, 500):
    for b in range(0, 500):
        if 1000 * (a + b - 500) == a*b:
            c = 1000 - a - b
            return a*b*c

print(special_pythagorean_triplet())

"""
0 < a < b < c

We know that a**2 + b**2 = c**2, also

a + b + c = 1000
c = 1000 - a - b, so

a**2 + b**2 = (1000 - a - b)**2
a**2 + b**2 = (1000 - a - b)*(1000 - a - b)
a**2 + b**2 = 10**6 - 1000a - 1000b - 1000a + a**2 + ab - 1000b + ab + b**2
0 = 10**6 - 1000a - 1000b - 1000a + ab - 1000b + ab
2000a + 2000b - 2ab - 10**6 = 0
2(1000a + 1000b - ab - 5*10**5) = 0
1000a + 1000b - ab - 5*10**5 = 0
1000a + 1000b - ab - 500*1000 = 0
1000(a + b - 500) - ab = 0
1000(a + b - 500) = ab

Since a,b > 0, then ab > 0 and thus (a + b - 500) > 0, so
a + b > 500
"""
