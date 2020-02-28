def high_and_low(numbers):
    # ...
    num = list(map(float, numbers.split()))
    return str(int(max(num))) + ' ' + str(int(min(num)))


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))