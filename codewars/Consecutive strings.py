def longest_consec(strarr, k):
    # your code
    # if len(strarr) == 0 or k > len(strarr) or k <= 0: return ""
    # if len(strarr) == k: return ''.join(strarr)
    # for i in range(len(strarr) - k + 1):
    #     for j in range(i + 1, i + k):
    #         strarr[i] += strarr[j]
    # return max(strarr, key=len)

    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result


# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta")
# print(longest_consec([], 3) == "")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) == "wlwsasphmxxowiaxujylentrklctozmymu")