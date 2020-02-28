def validBraces(string):
    dic = {')': '(', ']': '[', '}': '{'}
    list = []
    for i in string:
        if i in dic.values():
            list.append(i)
        if i in dic.keys():
            if len(list) == 0:
                return False
            if list.pop() != dic[i]:
                return False
    if len(list) == 0:
        return True


print(validBraces("()"), True);
print(validBraces("[(])"), False);
