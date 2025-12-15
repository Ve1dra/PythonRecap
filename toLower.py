def toLower(str):
    if str == '':
        return "Empty string input"
    lower = ''
    for i in str:
        if 'A' <= i <= 'Z':
            lower += chr(ord(i)+32)
        if i == ' ':
            lower += i
    print(lower)
    # return lower
toLower("THIS IS A TESTING STRING")
print(toLower(""))