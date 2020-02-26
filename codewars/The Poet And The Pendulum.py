def pendulum(values):
    values.sort()
    left = []
    right = []
    for i, val in enumerate(values):
        if i % 2 == 0:
            left.append(val)
        else:
            right.append(val)
    left.reverse()
    return left + right


#  [8,6,4,5,7]
print(pendulum([4,6,8,7,5]))