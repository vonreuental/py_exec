def next_happy_year(year):
    #your code here
    for i in range(year + 1, 9001):
        if len(set(str(i))) == 4:
            break
    return i


print(next_happy_year(1001))