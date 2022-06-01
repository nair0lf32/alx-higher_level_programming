#!/usr/bin/python3
for char in range(0, 100):
    if char == 99:
        print("99")
    else:
        print("{0:0=2d}, ".format(char), end='')
