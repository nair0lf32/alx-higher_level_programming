#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    for i in range(len(my_list)-1, -1, -1):
        print(my_list[i])
