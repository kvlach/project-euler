#!/usr/bin/env python3
from math import floor, sqrt


def trial_division(n):
    for s in range(2, floor(sqrt(n)) + 1):
        if n % s == 0:
            return s, n // s


def factorize(n):
    factors = []
    n = trial_division(n)
    while n:
        factors.append(n[0])
        trial = trial_division(n[1])
        if trial is None:
            factors.append(n[1])
            break
        else:
            n = trial

    return factors


print(factorize(600851475143))
