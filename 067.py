# Similar to Problem Eighteen, but with 100 rows so more elegance required
# Trade repeating work for space complexity, as low space complexity compared
# to redoing nearly every path calculation


def longestPath(depth, bottom, col):
    # hold left and right paths
    a = 0
    b = 0
    # if we are not at the bottom
    if bottom - depth != 1:
        # set path calculations to our cached solutions
        a = solved[depth + 1][col]
        # if the cached solutions don't exist, do the path check
        if a == -1:
            # store the path check in our cache, and set our left val correctly
            aPath = longestPath((depth + 1), bottom, col)
            solved[depth + 1][col] = aPath
            a += 1 + aPath
        # similar to b, but for col + 1
        b = solved[depth + 1][col + 1]
        if b == -1:
            bPath = longestPath((depth + 1), bottom, col + 1)
            solved[depth + 1][col + 1] = bPath
            b += 1 + bPath
    # add on value of root nodes, and check which is higher
    a += l[depth][col]
    b += l[depth][col]
    if a > b:
        return a
    else:
        return b

# for each test case
t = int(input())
for i in range(t):
    # for each row in triangle
    n = int(input())
    # if triangle is one row print the row/element
    if n == 1:
        print(input())
    # if triangle is multirow
    else:
        l = []
        solved = []
        for j in range(n):
            # append a series of lists that represent triangle
            l.append(list(map(int,input().split())))
            # also append a series of blank lists to act as storage for
            # solved paths so we don't redo work
            solved.append(list([-1]*(j+1)))
        # check path
        print(longestPath(0, n, 0))

