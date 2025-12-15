def toUper(str):
    if str == '':
        return "Empty string input"
    upper = ''
    for i in str:
        if 'a' <= i <= 'z':
            upper += chr(ord(i)-32)
        if i == ' ':
            upper += i
    print(upper)
    return upper
toUper('this is a testing string')
print(toUper(''))