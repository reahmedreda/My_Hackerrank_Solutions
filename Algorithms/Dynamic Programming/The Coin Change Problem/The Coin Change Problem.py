# Link : https://www.hackerrank.com/challenges/coin-change/problem
# Name : The Coin Change Problem
# Level : Medium
# Max Score : 60

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys
n, m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [1]+[0]*n
for i in range(m): 
    for j in range(coins[i], n+1): dp[j]+=dp[j-coins[i]]
print(dp[-1])
