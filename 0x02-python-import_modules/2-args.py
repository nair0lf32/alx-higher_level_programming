#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for a in range(1, argc + 1):
            print("{}: {}".format(a, sys.argv[a]))


if __name__ == "__main__":
    main()
