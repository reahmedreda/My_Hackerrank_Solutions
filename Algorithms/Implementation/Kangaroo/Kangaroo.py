# Link : https://www.hackerrank.com/challenges/kangaroo/problem
# Name : Kangaroo
# Level : Easy
# Max Score : 10

''''''''''''''''''''''''''''''''''''


#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if(v1>v2) and ((x2-x1)%(v1-v2)==0):
        print "YES"
    else :
        print "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
#print(result)
