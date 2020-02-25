def pig_it(text):
    # your code here
    t_list = text.split()
    for i, val in enumerate(t_list):
        if t_list[i].isalnum():
            t_list[i] = val[1:] + val[0:1] + 'ay'
    return ' '.join(t_list)


print(pig_it("O tempora o mores !"))
