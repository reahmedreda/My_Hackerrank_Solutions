# Link : https://www.hackerrank.com/challenges/utopian-tree/problem
# Name : Utopian Tree
# Level : Easy
# Max Score : 20

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python2

import sys


if __name__ == "__main__":
    n = int(raw_input())
    for _ in range(n):
        cycles = int(raw_input())
        k = cycles / 2
        m = 1 if cycles % 2 == 0 else 2
        print 2**(k+m) - m
