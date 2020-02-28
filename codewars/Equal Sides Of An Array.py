def find_even_index(arr):
    # your code here
    # if sum(arr[1:]) == 0: return 0
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return - 1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
print(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
