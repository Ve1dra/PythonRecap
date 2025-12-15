def countChar(str, c):
    if str == '':
        return "Empty string input"
    count = 0
    for i in range (len(str)):
        if str[i] == c:
            count +=1
    if not (c in str):
        return f"Character {c} is not in {str}" 
    return count
    
print(countChar("Abdulrasheed", 'e'))
print(countChar("Abdulrasheed", 'J'))
