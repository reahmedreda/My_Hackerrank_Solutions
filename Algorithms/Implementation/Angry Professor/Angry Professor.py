# Link : https://www.hackerrank.com/challenges/angry-professor/problem
# Name : Angry Professor
# Level : Easy
# Max Score : 20

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys

def angryProfessor(k, a):
    if k > sum([1 for i in a if i <=0]) : return ("YES") 
    else : return ("NO")
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
