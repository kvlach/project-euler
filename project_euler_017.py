def convert_num_to_words(n):
    core = [
        'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen'
    ]

    two_digit = [
        'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety'
    ]

    hundreds = [
        'one hundred', 'two hundred', 'three hundred',
        'four hundred', 'five hundred', 'six hundred',
        'seven hundred', 'eight hundred', 'nine hundred'
    ]

    if n in list(range(1, 20)):
        return core[n - 1]
    elif n in list(range(20, 100)):
        n1 = n // 10
        n2 = n % 10
        if n2 == 0:
            return f'{two_digit[n1-2]}'
        else:
            return f'{two_digit[n1-2]}-{core[n2-1]}'
    elif n in list((range(100, 1000))):
        n1 = n // 100
        n2 = (n % 100) // 10
        n3 = n % 10
        if (n2 == 0) and (n3 == 0):
            return f'{hundreds[n1-1]}'
        elif n2 in (0, 1):
            combine = 10*n2 + n3
            return f'{hundreds[n1-1]} and {core[combine-1]}'
        elif n3 == 0:
            return f'{hundreds[n1-1]} and {two_digit[n2-2]}'
        else:
            return f'{hundreds[n1-1]} and {two_digit[n2-2]}-{core[n3-1]}'
    else:
        return 'one thousand'


s = 0
for i in range(1, 1001):
    word = convert_num_to_words(i)
    word = word.replace(' ', '').replace('-', '')
    s += len(word)

print(s)
