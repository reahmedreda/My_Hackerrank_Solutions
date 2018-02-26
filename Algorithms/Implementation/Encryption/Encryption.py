# Link : https://www.hackerrank.com/challenges/encryption/problem
# Name : Encryption
# Level : Medium
# Max Score : 30

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys
import math 


        
if __name__ == "__main__":
    s = input().strip()
    sm=s.replace(" ","")
    r=math.floor(math.sqrt(len(sm)))
    c=math.ceil(math.sqrt(len(sm)))
    for i in range(c):
        print(sm[i::c],end=" ")  
