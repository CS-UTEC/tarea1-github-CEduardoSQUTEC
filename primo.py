import math

def isPrime(n):
    if n < 2:
        return False
    maxDivisor = math.floor(math.sqrt(n))
    for d in range (2, 1 + maxDivisor):
         if n % d == 0:
            return False
    return True
    
n = input("Enter a number: ")

if isPrime(int(n)):
    print("Is prime")
else:
    print('Is not prime')
