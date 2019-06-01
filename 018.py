def longestPath(depth, bottom, col):
    # if we are at the bottom, just return the node's number
    if bottom - depth == 1:
        a = l[depth][col]
        b = l[depth][col]
    else:
        # if we are not at the bottom, compare the node's number plus the
        # value of the paths going down the left and right children
        a = l[depth][col] + longestPath((depth + 1), bottom, col)
        b = l[depth][col] + longestPath((depth + 1), bottom, col + 1)
    # return higher value path
    if a > b:
        return a
    else:
        return b

# take in num of test cases
t = int(input())
for i in range(t):
    # take in num of rows for current triangle
    n = int(input())
    # for edge case of one row, print num
    if n == 1:
        print(input())
    # otherwise, take in each row and append as subsequent lists in an array
    else:
        l = []
        for j in range(n):
            l.append(list(map(int,input().split())))
        # check longest path rooted at head
        print(longestPath(0, n, 0))

