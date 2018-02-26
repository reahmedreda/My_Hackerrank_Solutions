# Link : https://www.hackerrank.com/challenges/nimble-game-1/problem
# Name : Nimble Game
# Level : Easy
# Max Score : 20

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys

def nimbleGame(a):
    # Complete this function
    b=0
    c=0
    for i in range(1,len(a)):
        if a[i] > 0:
            if a[i] % 2 == 0: c = 0
            else: c = i
            b = b ^ c
    if b == 0: return 'Second'
    else: return 'First'
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        s = list(map(int, input().strip().split(' ')))
        result = nimbleGame(s)
        print(result)
