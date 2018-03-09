# Link : https://www.hackerrank.com/challenges/lonely-integer/problem
# Name : Lonely Integer
# Level : Easy
# Max Score : 20 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python

import sys

def lonelyinteger(a):
    # Complete this function
    answer = reduce((lambda x, y: x^y), a)
    return answer

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = lonelyinteger(a)
print(result)
