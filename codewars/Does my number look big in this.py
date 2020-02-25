def narcissistic( value ):
    # Code away
    list = [int(x) for x in str(value)]
    res = 0
    for i in list:
        res += i ** len(list)
    return res == value

# return value == sum(int(x) ** len(str(value)) for x in str(value))


print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))