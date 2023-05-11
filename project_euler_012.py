from math import floor, sqrt
from itertools import count


def triangle_number(nth):
    """Returns nth triangle number"""
    return sum([i for i in range(1, nth+1)])


def divisors(n):
    divisors = [1, n]

    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


def highly_divisible_triangular_number(min_divisors):
    for i in count():
        triangle_num = triangle_number(i)
        num_of_divisors = len(divisors(triangle_num))
        if num_of_divisors > min_divisors:
            return triangle_num
    return


highly_divisible_triangular_number_500 = highly_divisible_triangular_number(500)
print(highly_divisible_triangular_number_500)
