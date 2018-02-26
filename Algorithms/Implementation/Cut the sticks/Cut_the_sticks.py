# Link : https://www.hackerrank.com/challenges/cut-the-sticks/problem
# Name : Cut the sticks
# Level : Easy
# Max Score : 25

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys

def cutTheSticks(arr):
    # Complete this function
    while(len(arr)):
        print(len(arr))
        arr = [x - min(arr) for x in arr if x - min(arr)>0]
        
          
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = cutTheSticks(arr)
    #print "\n".join(map(str, result))
