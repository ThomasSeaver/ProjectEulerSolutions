# precalculate all possible requests
sums = [0]*100001
# exactly one way to assemble a sum of 0
sums[0] = 1
# go through all possible coins, assembling an array of possibilities
# works like following
# starts off like  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# after 1p, like   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# because exactly one way to assemble each number with one pence coins
# after 2p, like   [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]
# because 2 ways to assemble 2, 3 ways to assemble 4, based on building
# from previous sum counts for 1p and 2p of lower numbers
# continues through all coins
for x in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(x, 100001):
        sums[i] += sums[i-x]

# take in input, go through pre-calc array to get answer
t = int(input())
for _ in range(t):
    money = int(input())
    print(sums[money] % ((10 ** 9) + 7))

