#!/usr/bin/python3
for char in range(0, 10):
    for char2 in range(0, 10):
        if char >= char2:
            continue
        elif char == 8 and char2 == 9:
            print("{}{}".format(char, char2))
        else:
            print("{}{}, ".format(char, char2), end='')
