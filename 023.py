import math

# keep track of our abundant numbers
abundantNums = []

# build a list of abundant numbers < 15000, because we know by mathematical
# analysis that every number > 28123 can be summed from two abundant numbers,
# so we just have to check up to 15000 for potential half of sums
for i in range(1, 15000):
    # include one as divisor by default, check from 2 to sqrt
    divisorSum = 1
    j = 2
    # find divisors, sum them up, and if they are greater than num, add to list
    while j <= math.sqrt(i):
        # if it is a divisor
        if i % j == 0:
            # add divisor sum, and check if it is not the sqrt
            divisorSum += j
            if i // j != j:
                # if not sqrt, add the secondary divisor as well
                divisorSum += i // j
        j += 1
    if i < divisorSum:
        # add to our cache of abundant sums
        abundantNums.append(i)

# for each test case
t = int(input())
for _ in range(t):
    n = int(input())
    # if number isnt proven via math analysis
    if n <= 28123:
        # go through list, comparing each pair of possible nums from front to
        # back of list
        l = 0
        check = 0
        r = len(abundantNums) - 1
        # while we are still checking numbers
        while r >= 0:
            # if one num is higher than sum, move it down
            if abundantNums[r] > n:
                r -= 1
            else:
            # otherwise check all numbers under it
                l = 0
                while l <= r:
                    # if our sum is higher, we are lost, as list is ordered
                    if abundantNums[l] + abundantNums[r] > n:
                        l = r + 1
                    # if our sum is matching, exit and mark for yes
                    elif abundantNums[l] + abundantNums[r] == n:
                        l = r + 1
                        r = -1
                        check = 1
                    # otherwise move up for next comparison
                    else:
                        l += 1
                r -= 1
        if check == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")


