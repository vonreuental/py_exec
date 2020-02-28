def solution(number):
    i = sum = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1
    return i


print(solution(10))
