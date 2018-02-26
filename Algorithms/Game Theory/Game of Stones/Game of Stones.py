# Link : https://www.hackerrank.com/challenges/game-of-stones-1/problem
# Name : Game of Stones
# Level : Easy
# Max Score : 15

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys

def gameOfStones(n):
    
    if(n%7>=2):return "First"
    else : return "Second"
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        print(result)
