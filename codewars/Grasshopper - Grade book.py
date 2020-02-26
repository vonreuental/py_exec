def get_grade(s1, s2, s3):
    # Code here
    grade = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'F'}
    return grade[[i for i in grade if (s1 + s2 + s3) / 3 >= i][0]]


print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(70, 70, 70))