def isPrime(num) :
    if num == 0 or num == 1:
        return -1
    if num < 0:
        num = -num
        for i in range(2, num):
            if num % i == 0:
                return f'{num} is not a prime number'
            elif num % num or num % 1 == 0:
                return f'{num} is a prime number'
    elif num > 0:
        for i in range(2, num):
            if num % i == 0:
                return f'{num} is not a prime number'
            elif num % num or num % 1 == 0:
                return f'{num} is a prime number'
    elif num != '0' and num != '9':
        return "Invalid input"
    
print(isPrime(100))
print(isPrime(111))
print(isPrime(1))
print(isPrime(0))
print(isPrime(-5))