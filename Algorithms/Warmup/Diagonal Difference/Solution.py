
import sys

s=0
n = int(raw_input().strip())
matrix = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    matrix.append(a_temp)
l = len(matrix[0])
x= [matrix[i][i] for i in range(l)]              
y= [matrix[l-1-i][i] for i in range(l-1,-1,-1)]
for k in xrange(l):
    s=s+(y[k]-x[k])
print abs(s)
