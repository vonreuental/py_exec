def dig_pow(n, p):
    # your code
    sum = 0
    for i, val in enumerate(str(n)):
        sum += int(val) ** (p + i)
    return sum // n if sum % n == 0 else -1


print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)