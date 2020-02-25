from collections import Counter


def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


#     c1 = Counter(filter(str.islower, s1))
#     c2 = Counter(filter(str.islower, s2))
#     res = []
#     for c in set(c1.keys() + c2.keys()):
#         n1, n2 = c1.get(c, 0), c2.get(c, 0)
#         if n1 > 1 or n2 > 1:
#             res.append(('1', c, n1) if n1 > n2 else
#                 ('2', c, n2) if n2 > n1 else ('=', c, n1))
#     res = ['{}:{}'.format(i, c * n) for i, c, n in res]
#     return '/'.join(sorted(res, key=lambda s: (-len(s), s)))


# "2:eeeee/2:yy/=:hh/=:rr"
print(mix("Are they here", "yes, they are here"))