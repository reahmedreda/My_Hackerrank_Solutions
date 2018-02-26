import sys

def miniMaxSum(arr):
    x=0
    y=0
    # Complete this function
    arr.sort()
    x=sum(arr[i] for i in range(1,len(arr) ))
    y=sum(arr[i] for i in range(0,len(arr)-1 ))
    print str(y) + " " + str(x)

if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)
