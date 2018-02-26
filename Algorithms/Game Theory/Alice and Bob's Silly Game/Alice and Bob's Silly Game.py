# Link : https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem
# Name : Alice and Bob's Silly Game
# Level : Meduim
# Max Score : 30

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3
import sys

def sieve(num):
    my_list = [1]*(num+1)
    my_list[0] = 0
    for i in range(2,int(num**0.5)+1):
        if my_list[i] == 1:
            for j in range(i*i,num+1,i):
                my_list[j] = 0
    return my_list

g = int(input().strip())
sieve_list = sieve(100000)
for a0 in range(g):
    n = int(input().strip())
    # your code goes here
    used_list = sum(sieve_list[1:n+1])
    if used_list % 2 ==1:
        print("Bob")
    else:
        print("Alice")
