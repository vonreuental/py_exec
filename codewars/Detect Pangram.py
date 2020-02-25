import string


def is_pangram(s):
    # return len(''.join(set(filter(str.isalpha, s.upper())))) == 26
    return set( string.ascii_lowercase) <= set(s.lower())


pangram = "The quick, brown fox jumps over the lazy dog! "
print(is_pangram(pangram))