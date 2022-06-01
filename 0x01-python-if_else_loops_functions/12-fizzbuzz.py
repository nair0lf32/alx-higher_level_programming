#!/usr/bin/python3
def fizzbuzz():
    for char in range(1, 101):
        if char % 3 == 0 and char % 5 == 0:
            print("FizzBuzz", end=' ')
        elif char % 5 == 0:
            print("Buzz", end=' ')
        elif char % 3 == 0:
            print("Fizz", end=' ')
        else:
            print("{}".format(char), end=' ')
