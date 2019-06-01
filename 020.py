import math

t = int(input())
for i in range(t):
    n = int(input())
    fact = math.factorial(n)
    sumTotal = 0
    while fact > 0:
        sumTotal += fact % 10
        fact = fact // 10
    print(sumTotal)
