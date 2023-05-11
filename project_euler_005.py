from math import gcd
from functools import reduce


def LCM(*lst):
    def lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm, *lst)


smallest_multiple_20 = LCM(range(1, 21))
print(smallest_multiple_20)
