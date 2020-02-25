# def persistence(n, count):
#     # your code
#     str_n = str(n)
#     if len(str_n) <= 1:
#         return count
#     num = 1
#     for i in str_n:
#         num *= int(i)
#     count += 1
#     return persistence(num, count)


def persistence(n):
    # your code
    str_n = str(n)
    count = 0
    while len(str_n) >= 1:
        num = 1
        for i in str_n:
            num *= int(i)
        str_n = str(num)
    return count


print(persistence(39))