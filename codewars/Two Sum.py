def two_sum(numbers, target):
    # start coding!
    d = {}
    for i, val in enumerate(numbers):
        another_tar = target - val
        if another_tar in d:
            return [d[another_tar], i]
        d[val] = i


print(two_sum([1234, 5678, 9012], 14690))