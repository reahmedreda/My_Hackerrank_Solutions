# Link : https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Name : Bigger is Greater
# Level : Medium
# Max Score : 35

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys

def biggerIsGreater(s):
    
    h = False
    for i in range(len(s)-1)[::-1]:
        if ord(s[i]) < ord(s[i+1]):
            for j in range(i+1,len(s))[::-1]:
                if ord(s[i]) < ord(s[j]):
                    lis = list(s)
                    lis[i],lis[j]=lis[j],lis[i]
                    print("".join(lis[:i+1]+lis[i+1:][::-1]))
                    h = True
                if h == True:
                    break
        if h == True:
            break
    if h == False:
        print("no answer")

if __name__ == "__main__":
    T = int(raw_input().strip())
    for a0 in xrange(T):
        w = raw_input().strip()
        result = biggerIsGreater(w)
