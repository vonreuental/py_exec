# def rgb(r, g, b):
#     #your code here :)
#     rgb = [r, g, b]
#     for i, val in enumerate(rgb):
#         if val > 255:
#             val = 255
#         elif val < 0:
#             val = 0
#         rgb[i] = hex(val)[2:].zfill(2).upper()
#     return "".join(rgb)


def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))



print(rgb(-20, 275, 125))