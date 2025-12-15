print("Hello World\n")

def isAlpha(str) :
    if str == "":
        return "Empty string input"
    alpha = ''
    for i in (str) :
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') :
            alpha += i
    if alpha == '' :
        return "No alphabets here"
    
    return f'The alphabet in {str} is {alpha}'

def countAlpha(str) :
    if str == "":
        return "Empty string input"
    alpha = ''
    for i in (str) :
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') :
            alpha += i
    if alpha == '' :
        return "No alphabets here"
    
    return f'The alphabet in {str} is {len(alpha)}'

print(isAlpha(""), '\n')
print(isAlpha("2yi2"), '\n')
print(isAlpha("02D92"), '\n')
print(isAlpha("UzU"), '\n')
print(isAlpha("-BBA"), '\n')
print(isAlpha("Abcd"), '\n')
print(isAlpha("Zbcd"), '\n')

print(isAlpha("I LOVE PYTHON"))


print(countAlpha(""), '\n')
print(countAlpha("2yD2"), '\n')
print(countAlpha("0o"), '\n')
print(countAlpha("7zU"), '\n')
print(countAlpha("0BBA"), '\n')
print(countAlpha("0bcd"), '\n')
print(countAlpha("5bcd"), '\n')

print(countAlpha("I LOVE PYTHON"))