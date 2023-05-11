from math import floor, sqrt


def prime_sieve(n):
    prime_array = n * [True]

    for i in range(2, n+1):
        if prime_array[i-1] is True:
            for j in range(i+i, n+1, i):
                prime_array[j-1] = False

    return [i+1 for i, item in enumerate(prime_array) if item == True][1:]

s = sum(prime_sieve(2000000))
print(s)
