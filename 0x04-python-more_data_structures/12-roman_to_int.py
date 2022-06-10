#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    romans_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for char in range(len(roman_string)):
        if char > 0 and romans_keys[roman_string[char]] > romans_keys[roman_string[char - 1]]:
            value += romans_keys[roman_string[char]] - 2 * romans_keys[roman_string[char - 1]]
        else:
            value += romans_keys[roman_string[char]]
    return value
