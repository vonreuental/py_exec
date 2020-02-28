def likes(names):
#     #your code here
#     if len(names) >= 4:
#         return names[0] + ',' + names[1] + ' and 2 others like this'
#     elif len(names) == 3:
#         return names[0] + ',' + names[1] + ' and' + names[2] + ' like this'
#     elif len(names) == 2:
#         return names[0] + ',' + names[1] + ' like this'
#     elif len(names) == 1:
#          return names[0] + ' like this'
#     else:
#         return 'no one likes this'
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n - 2)




print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')