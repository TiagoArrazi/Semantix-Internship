from math import sqrt, floor
from sys import argv

def Fibonacci(n):

    return int(floor(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))+0.5))


try:

    print(Fibonacci(int(argv[1])))

except OverflowError as e:

    print(e)
