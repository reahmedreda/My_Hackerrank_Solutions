# Link : https://www.hackerrank.com/challenges/strange-code/problem
# Name : Strange Counter
# Level : Easy
# Max Score : 30 

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys


def strangeCode(t):
    # Complete this function
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2

    return(rem-t+1)
    
    

if __name__ == "__main__":
    t = long(raw_input().strip())
    result = strangeCode(t)
    print result
