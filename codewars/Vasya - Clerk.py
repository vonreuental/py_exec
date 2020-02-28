def tickets(people):
    dic = {25: 0, 50: 0}
    for i in people:
        if i == 100:
            if dic[50] >= 1 and dic[25] >= 1:
                dic[50] -= 1
                dic[25] -= 1
            elif dic[25] >= 3:
                dic[25] -= 3
            else:
                return 'NO'
        if i == 50:
            if dic[25] >= 1:
                dic[25] -= 1
                dic[50] += 1
            else:
                return 'NO'
        if i == 25:
            dic[25] += 1
    return "YES"


print(tickets([25, 25, 50]), "YES")
print(tickets([25, 100]), "NO")
