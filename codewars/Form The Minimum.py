def min_value(digits):
    # your code here
    # res = sorted(set(digits))
    # sum = 0
    # for i, val in enumerate(res):
    #     sum += val * 10 ** (len(res) - i - 1)
    # return sum

    return int(''.join(map(str, sorted(set(digits)))))


print(min_value([1, 3, 1]))