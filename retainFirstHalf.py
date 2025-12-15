def retainFirstHalf(str):
    str = str.strip()
    if str == '':
        return "Empty string input"
    if len(str) == 1:
        return str
    
    count = len(str)
    if count % 2 != 0:
        median = (count + 1) / 2
        meed = int(median)
        g = str[0:meed]
        print(g)
    elif count % 2 == 0:
        median = count/2
        meed = int(median)
        g = str[0:meed]
        print(g)
    
    
print(retainFirstHalf(""), '\n')
print(retainFirstHalf("This is a testing string"), '\n')
print(retainFirstHalf("                   another testing function"))

s = "Hello, Python"
home = len(s)
split = s[0:home-5]
print(split)
