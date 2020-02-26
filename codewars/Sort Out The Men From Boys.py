def men_from_boys(arr):
    #your code here
    men = []
    boys = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            men.append(i)
        else:
            boys.append(i)
    return men + boys[::-1]


print(men_from_boys([7,3,14,14,17]))