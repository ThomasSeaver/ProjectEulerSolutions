
# prep for storing resulting values
results = [[0 for i in range(500)] for j in range(500)]

# set all values in first row/col to 1 as there is only one path along a single line
for i in range(500):
    results[i][0] = 1;
for j in range(500):
    results[0][j] = 1;

# now go throughout and add up number of paths to above and left to get paths to here
# preprocessed because up to 1000 test cases means we could have worst case a lot,
# rather than just caching values once and having O(1) solves
for i in range(1, 500):
    for j in range(1, 500):
        results[i][j] = results[i-1][j] + results[i][j-1]

# take input, split along delimiter, listify, map to int, then list again
# throw input to cached array and print result mod 10^9 + 7
t = int(input())
for i in range(t):
    sizes = list(map(int, list(input().split())))
    print(results[sizes[0]][sizes[1]] % (1000000007))
