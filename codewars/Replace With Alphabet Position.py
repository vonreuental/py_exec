def alphabet_position(text):
    return ' '.join([(str(ord(i) - 64)) for i in filter(str.isalpha, text.upper())])


print(alphabet_position("The sunset sets at twelve o' clock."))