#!/bin/python3

import sys

# Take in num of nums
t = int(input().strip())
for a0 in range(t):
    # access first num, but subtract one since we only want natural number below it
    n = int(input().strip()) - 1
    # Grabbing summation of 3's and 5's possible in one step
    # This is because all summations follow pattern of (0, 3, 6, 9...)
    # can use summations of numbers below n then multiply by 3/5/15
    # Because 3 and 5 both count multiples of 15, we must subtract it once from our final
    threes = int(3*(n//3)*(n//3 + 1)//2)
    fives = int(5*(n//5)*(n//5 + 1)//2)
    fifteens = int(15*(n//15)*(n//15 + 1)//2)
    result = threes + fives - fifteens;
    print(result)

