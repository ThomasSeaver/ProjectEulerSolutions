# had to remember how quadratics work for this one lol

# for each test case
t = int(input())
for _ in range(t):
    # take in our width/height of our spiral
    n = int(input())
    # convert it so that it represents whichever i'th odd number it is
    # 3 -> 2, 5 -> 3, 7 -> 4, etc.
    # this is because we are modeling the sequence of numbers to the left
    # of the spiral, and those go by 1 rather than by 2
    n = 1 + ((n - 1) // 2)

    # for example if we have the spiral
    # 21 22 23 24 25
    # 20  7  8  9 10
    # 19  6  1  2 11
    # 18  5  4  3 12
    # 17 16 15 14 13

    # if we want the diagonals of the spiral, we can see that the number to the
    # left times four will always be equivalent to the sum of the diagonal vals
    # this is because its the midpoint between the upper left and the bottom
    # left pair, as well as between the upper right and lower right pair

    # thus, if we can model the sequence, and then sum the values we get,
    # and multiply it by 4, we will have an answer to our diagonal sum problem
    # in O(1)

    # we can model the sequence 1, 6, 19, 40, 69 with a quadratic equation
    # This is becasue while the diff between the numbers goes as
    # 5, 13, 21, 29
    # where the first diff is always changing, we note the second diff as
    # 8,  8,  8,  8
    # so a quadratic formula is perfect

    # if you need a review I suggest this link that I found which helped
    # https://www.youtube.com/watch?time_continue=634&v=FfCq7bGAFoY

    # from there we find our formula to be 4n^2 - 7n + 4
    # Utilizing summations and derivations of Gauss's formula for sequences,
    # we find the sum of squares up to n
    firstTerm = (n * (n + 1) * (2 * n + 1)) // 6
    # sum of numbers 1, 2, 3, ..., n
    secondTerm = ((n * (n + 1)) // 2)
    # and just n itself
    thirdTerm = n
    # and plug these totals into our quadratic formula
    # because the sequence's goal is to be a model for the diagonals,
    # we must multiply it by 4. However, the first element, 1, is the only
    # non diagonal having value. Therefore, we must subtract and re-add it
    summation = 4 * ((4 * firstTerm - 7 * secondTerm + 4 * thirdTerm) - 1) + 1
    # lastly, mod these incredibly large values, and print
    print(summation% (pow(10, 9) + 7))