def sum_squre_difference(upper_bound):
    lst = list(range(1, upper_bound + 1))
    square_of_sum = sum(lst)**2
    sum_of_squares = sum([i*i for i in lst])

    return square_of_sum - sum_of_squares

sum_squre_difference_100 = sum_squre_difference(100)
print(sum_squre_difference_100)
