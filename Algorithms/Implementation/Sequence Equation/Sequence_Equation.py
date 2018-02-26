# Link : https://www.hackerrank.com/challenges/permutation-equation/problem
# Name : Sequence Equation
# Level : Easy
# Max Score : 20 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys

n = int(input())
numbers = [int(num) for num in input().split()]

for x in range(n):
    print(numbers.index(numbers.index(x + 1) + 1) + 1)
