# Enter your code here. Read input from STDIN. Print output to STDOUT
# take in num of input
t = int(input())
for i in range(t):
    # for each input
    n = int(input())
    # store summation, and number to break down
    summing = 0
    exp = 2 ** n
    while exp > 0:
        # while number is not broken down,
        # add least significant digit to sum, and divide away
        summing += exp % 10
        exp = exp // 10
    # print result
    print(summing)

