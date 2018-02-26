
import sys

def staircase(n):
    # Complete this function
    for i in xrange(n):
        print ((n-i-1)* " ") + ((i+1)*"#")

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)
