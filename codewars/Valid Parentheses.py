def valid_parentheses(string):
    # your code here

    # bracket = {')': '('}
    # bracket_l, bracket_r = bracket.values(), bracket.keys()
    #
    # arr = []
    # for c in string:
    #     if c in bracket_l:
    #         # 左括号入栈
    #         arr.append(c)
    #     elif c in bracket_r:
    #         # 右括号，要么栈顶元素出栈，要么匹配失败
    #         if arr and arr[-1] == bracket[c]:
    #             arr.pop()
    #         else:
    #             return False
    # if len(arr) > 0:return False
    # return True
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


print(valid_parentheses("  ("))
print(valid_parentheses("hi(hi)()"))