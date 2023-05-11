#!/usr/bin/env python3


def fibonacci(n):
    a, b = 1, 2
    while b < n:
        a, b = b, a + b
        yield a


s = sum([i for i in fibonacci(4*10**6) if i % 2 == 0])

print(s)
