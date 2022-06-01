#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(i)
        if char >= 97 and char <= 122:
            char -= 32
        char = chr(char)
        print("{}".format(char), end='')
    print("")
