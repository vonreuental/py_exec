def get_middle(s):
    #your code here
    if len(s) <= 2:
        return s
    if len(s) % 2 == 0:
        return s[len(s)//2:len(s)//2 + 2]
    else:
        return s[len(s)//2]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))