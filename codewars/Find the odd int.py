from collections import Counter


def find_it(seq):
    dic = Counter(seq)
    for i in dic.values():
        if i % 2 == 1:
            return list(dic.keys())[list(dic.values()).index(i)]


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))