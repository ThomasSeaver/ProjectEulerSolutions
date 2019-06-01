import math

# we have to keep track of our divisor sums so we can check for amicable num
# and we have to keep track of total sums so we can provide solutions
divisorSums = [0]
totalSums = [0]

# pre-calculate, as amicable numbers under n can have a second half higher
# than bound. also up to a thousand test cases, so caching more efficient
totalSum = 0
for i in range(1, 100000):
        # include one as divisor by default, check from 2 to sqrt
        divisorSum = 1
        j = 2
        while j <= math.sqrt(i):
            # if it is a divisor
            if i % j == 0:
                # add divisor sum, and check if it is not the sqrt
                divisorSum += j
                if i // j != j:
                    # if not sqrt, add the secondary divisor as well
                    divisorSum += i // j
            j += 1
        # add to our cache of divisor sums
        divisorSums.append(divisorSum)
        # if our divisor sum is smaller than our original number, we know
        # this has potential to be the second of two amicable numbers
        # check our cache to see if they line up
        if divisorSum < i and divisorSums[divisorSum] == i:
            # if they do, go back and for all nums between our amicable numbers,
            # add the lower amicable number to our cached sums
            for k in range(divisorSum + 1, i):
                totalSums[k] += divisorSum
            # also increment our total sum counter as normal for future bounds
            totalSum += i + divisorSum
        totalSums.append(totalSum)


# simply take in test cases and output cached values
t = int(input())
for i in range(t):
    n = int(input())
    print(str(totalSums[n]))








