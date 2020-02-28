def iq_test(numbers):
    # your code here
    list = numbers.split()
    for i in range(len(list) - 1):
        list[i] = int(list[i + 1]) - int(list[i])
    list.pop()
    for j, val in enumerate(list):
        if list.count(val) == 1:
            return j + 1 if j == 0 else j + 2


print(iq_test("2 4 7 8 10"), 3)
print(iq_test("1 2 2"), 1)
