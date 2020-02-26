def run(tricks):
    dict = {}
    for run in tricks:
        count = 0
        times = 0
        point = run['points']
        while True:
            now_point = run['probability'] ** (times + 1) * point
            if now_point > count:
                count = now_point
            else:
                break
            times += 1
            point += run['points'] * run['mult_base'] ** times
        dict['kickflip'] = times
    return dict


# { 'kickflip': 8, }
print(run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },]))