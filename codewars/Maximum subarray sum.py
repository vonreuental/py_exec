def max_sequence(arr):
    # ...
    if arr == [] or max(arr) < 0:
        return 0
    dp = [0 for i in (range(len(arr) + 1))]
    dp[0] = float("-inf")
    for i in range(1, len(arr) + 1):
        dp[i] = max(dp[i - 1] + arr[i - 1], arr[i - 1])
    return max(dp)

    # max, curr = 0, 0
    # for x in arr:
    #     curr += x
    #     if curr < 0:
    #         curr = 0
    #     if curr > max:
    #         max = curr
    # return max


# 6 [4, -1, 2, 1]
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
