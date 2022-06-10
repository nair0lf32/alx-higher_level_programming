#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    li = list(map(lambda n: n * number, my_list))
    return li
