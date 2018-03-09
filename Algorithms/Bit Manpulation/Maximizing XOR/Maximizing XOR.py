# Link : https://www.hackerrank.com/challenges/maximizing-xor/problem
# Name : Maximizing XOR
# Level : Easy
# Max Score : 30 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python

import sys

def maximizingXor(l, r):
    # Complete this function
    return max([x^y for x in range(l,r+1)  for y in range(l,r+1) ])

if __name__ == "__main__":
    l = int(raw_input().strip())
    r = int(raw_input().strip())
    result = maximizingXor(l, r)
    print result
