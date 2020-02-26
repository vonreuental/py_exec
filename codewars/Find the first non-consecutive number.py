def first_non_consecutive(arr):
    #your code here
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            continue
        else:
            return arr[i]
        return None


print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
print(first_non_consecutive([4,6,7,8,9,11]))
print(first_non_consecutive([4,5,6,7,8,9,11]))
print(first_non_consecutive([31,32]))
print(first_non_consecutive([-3,-2,0,1]))
print(first_non_consecutive([-5,-4,-3,-1]))

print(float("-234.4"))