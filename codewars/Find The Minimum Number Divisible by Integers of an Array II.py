def min_special_mult(arr):
    # your code here
    new_list = []
    for i in arr:
        if i.

    greater = max(arr)
    while True:
        if not list(filter(lambda i: greater % i != 0, arr)):
            return greater
        greater += 1


arr = [2, 3, 4, 5, 6, 7]
print(min_special_mult(arr), 420)

arr = [18, 22, 4, 3, 21, 6, 3]
print(min_special_mult(arr), 2772)

arr = [16, 15, 23, 'a', '&', '12']
print(min_special_mult(arr), "There are 2 invalid entries: ['a', '&']")

arr = [16, 15, 23, 'a', '&', '12', 'a']
print(min_special_mult(arr), "There are 3 invalid entries: ['a', '&', 'a']")

arr = [16, 15, 23, 'a', '12']
print(min_special_mult(arr), "There is 1 invalid entry: a")

arr = [16, 15, 23, '12']
print(min_special_mult(arr), 5520)

arr = [16, 15, 23, '012']
print(min_special_mult(arr), 5520)

arr = [18, 22, 4, None, 3, 21, 6, 3]
print(min_special_mult(arr), 2772)

arr = [18, 22, 4, None, 3, -21, 6, 3]
print(min_special_mult(arr), 2772)

arr = [16, 15, 23, '-012']
print(min_special_mult(arr), 5520)
