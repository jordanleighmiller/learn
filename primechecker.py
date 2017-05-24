#!/usr/bin/env python3

# FUNCTION: checkprime
# ARGS: number = number to check if prime
# RETURNS:
# true: if number is prime
# false: if number is NOT prime
def checkprime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

N = 0

while N != -1:

    N = int(input("Input a number: "))

    if checkprime(abs(N)):
        print ("%d is prime." % N)
    else:
        print("%d is NOT prime." % N)
