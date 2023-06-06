#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of"
ld = number % 10
if number < 0:
    ld = abs(number) % 10
    ld *= -1
if ld > 5:
    print(s, number, "is", ld, "and is greater than 5")
elif ld == 0:
    print(s, number, "is", ld, "and is 0")
else:
    print(s, number, "is", ld, "and is less than 6 and not 0")
