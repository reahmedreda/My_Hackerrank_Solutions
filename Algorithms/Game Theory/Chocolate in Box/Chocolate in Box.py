# Link : https://www.hackerrank.com/challenges/chocolate-in-box/problem
# Name : Chocolate in Box
# Level : Medium
# Max Score : 70

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python2


n,a,b = input(),map(int, raw_input().split()),0
for i in a: b ^= i
print sum([int(i^b < i) for i in a])
