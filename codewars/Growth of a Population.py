def nb_year(p0, percent, aug, p):
    # your code
    count = 0
    sum = p0
    while sum <= p:
        sum = (sum * (1 + percent / 100) + aug) 
        count += 1
        continue
    return count


print(nb_year(1500, 5, 100, 5000))