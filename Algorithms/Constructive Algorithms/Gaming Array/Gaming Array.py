# Link : https://www.hackerrank.com/challenges/an-interesting-game-1/problem
# Name : Gaming Array
# Level : Medium
# Max Score : 35 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys


g = int(input().strip())
w=["BOB","ANDY"]
winner=w[0]
f=True 
for a0 in range(g):
    f=True
    arr=[]
    max=0
    n = int(input().strip())
    arr=(input().strip().split())
    arr=list(map(int,arr))

    for i in range(n):
        if(max<arr[i]):
            max=arr[i]
                   
            f=not f
    if(f):print(w[1])
    else : print (w[0])
