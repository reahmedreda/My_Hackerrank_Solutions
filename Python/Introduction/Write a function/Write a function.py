# Link : https://www.hackerrank.com/challenges/write-a-function/problem
# Name : Write a function
# Level : Meduim
# Max Score : 10


''''''''''''''''''''''''''''''''''''
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
