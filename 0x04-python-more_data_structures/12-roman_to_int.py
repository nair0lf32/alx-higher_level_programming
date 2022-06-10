#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for c in range(len(roman_string)):
        if c > 0 and dic[roman_string[c]] > dic[roman_string[c - 1]]:
            value += dic[roman_string[c]] - 2 * dic[roman_string[c - 1]]
        else:
            value += dic[roman_string[c]]
    return value
