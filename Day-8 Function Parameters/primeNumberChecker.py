import math

def prime(num):
    if num <= 1:
        print(f"{num} is not a prime number")
        return
    
    isPrime = True
    for n in range (2, math.isqrt(num) + 1):
        if num % n == 0 :
            isPrime = False
            break
    
    if isPrime :
        print(f"{num} is a prime number")
    else :
        print(f"{num} is not a prime number")

num = int(input("Enter the number you want to check wather it is prime or not? "))

prime(num)