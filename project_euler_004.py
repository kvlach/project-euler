def check_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def biggest_palindrome_number(digits):
    num = 0
    lower = 10**(digits-1)
    upper = 10**digits
    for i in range(lower, upper):
        for j in range(lower, upper):
            prod = i*j
            if prod > num and check_palindrome(str(prod)):
                num = prod
    return num


three_digit_palnidrome = biggest_palindrome_number(4)
print(three_digit_palnidrome)
