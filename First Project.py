# imports
import random
import math

# initiate variables
from typing import Any

a = []
b = 0
x = 0
# initialize functions


# takes second of list
def take_second(elem):
    return elem[1]


# does the log2
def log2(list):
    return int(math.log2(len(list)))


try:
    # initialize list
    for i in range(16):
        a.append([i, 0])
    random.shuffle(a)
    # debug
    print(a)
    # big tournament of numbers
    for i in range(log2(a)):
        while x + 1 < len(a):
            # it adds points to the higher depending to the 'difficulty' of the round
            if a[x][0] > a[x + 1][0]:
                a[x][1] += int(math.pow(2, i))
            else:
                a[x + 1][1] += int(math.pow(2, i))
            x += 2
        x = 0
        a.sort(key=take_second, reverse=True)
    print(a)

except IndexError:
    print("Something's wrong with the index")
