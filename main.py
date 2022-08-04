
from utilities import *
from shopping.shopping_cart import *
import random

print(dir(random))

if __name__ == '__main__':
    x=2
    y=3

    print("X*Y=", multiply(x, y))
    print("X/Y=", divide(x, y))

    print("You purchased:", buy(input("What did you buy? ")))






