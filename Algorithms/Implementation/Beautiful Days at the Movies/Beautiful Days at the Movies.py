# Link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Name : Beautiful Days at the Movies
# Level : Easy
# Max Score : 15

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#!/bin/python3

import sys
i, j, k = [int(x) for x in input().split()]
beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
print(sum(beautifulDays))
