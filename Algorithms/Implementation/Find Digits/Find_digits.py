# Link : https://www.hackerrank.com/challenges/find-digits/problem
# Name : Find Digits
# Level : Easy
# Max Score : 25 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys

def findDigits(n):
    # Complete this function
    
    return sum([1 for i in map(int, list(str(n))) if i != 0 and  n% i == 0])

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input())
        result = findDigits(n)
        print result
