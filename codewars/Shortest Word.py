def find_short(s):
    # your code here
    return min(len(x) for x in s.split())


print(find_short("bitcoin take over the world maybe who knows perhaps"))