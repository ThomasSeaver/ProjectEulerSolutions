# took me a while to figure this one out
# trouble mostly came from implementation of brute force method and figuring
# how to do it
# could clean it up to be less stupid and brute forcey, but it works pretty
# fast as is

# so we need to check for pandigital options
# this method is janky, but I needed to figure out a way to fill various mults
# up with every possible num, then pass a modified list down, to fill up the
# remaining places, and this seemed like the best way

# left represents the remaining places to fill in our first mult
# right represents the remaining places to fill in our second mult
# multA is our left multiplier
# multB is our right multiplier
# nums is the current list of possible nums to pull from
def checkPandigital(left, multA, right, multB, nums):
    # summation will be our list of products we pass back
    summation = []
    # if we have places to fill in our left mult,
    if (left != 0):
        # go through every num we can pull from
        for num in nums:
            # copy the list as is, remove the current num, and add it to our
            # current left mult
            numscopy = nums.copy()
            numscopy.remove(num)
            multAcopy = multA + str(num)
            # pass this modified mult, numslist, and left count, down to be
            # filled. In this way, we will go through every possible num
            # in our list and place it in this space
            summation.extend(checkPandigital(left - 1, multAcopy, right, multB, numscopy))
        return summation
    # if we have spaces in our right and our left is full,
    elif (right != 0):
        for num in nums:
            # copy the list as is, remove the current num, and add it to our
            # current right mult
            numscopy = nums.copy()
            numscopy.remove(num)
            multBcopy = multB + str(num)
            # pass this modified mult, numslist, and right count, down to be
            # filled. In this way, we will go through every possible num
            # in our list and place it in this space

            # the other possible place for duplicates occurs when the lengths
            # of mults are the same, so we may accidentally test 2 * 1 again,
            # for example. This is not ideal, so we check a few things

            # if we have more places to fill in the right, we're not creating
            # a duplicate yet. If our multiplier on the left is less than our
            # right multiplier, we are not creating a duplicate. If our lengths
            # are different, we're also not creating a duplicate.
            # in this way we keep the extra duplicates out of the recursive call
            if (right - 1 != 0 or multA < multBcopy or len(str(multA)) != len(str(multBcopy))):
                summation.extend(checkPandigital(left, multA, right - 1, multBcopy, numscopy))
        return summation
    # if we have two full multipliers,
    else:
        # multiply them
        product = int(multA) * int(multB)
        # check if theyre the same length as our remaining num list
        if (len(nums) == len(str(product))):
            # break the product into a list of individual digits, and sort
            productList = [int(d) for d in str(product)]
            productList.sort()
            # if they're equivalent, we have a pandigital product. Return it.
            # else, return empty lists.
            if (productList == nums):
                return [product]
            else:
                return []
        else:
            return []



# take in input and set up answer list
n = int(input())
answer = []

# because we're looking for pandigital numbers, we need two multiplication units
# obviously the answer must have at least one digit, so we find two mults that
# have lengths maxing out at a sum of n-1

# we do this by having a range go from 1 -> n//2 + 1 so that it will go up to
# the halfway point of the num
# and a range that goes from the previous number up to n - that number
# in this way we get assortments of appropriate mult lengths.

# for example, inputting 5 would get you [1, 1], [1, 2], [1, 3], [2, 2]
# because we are starting from x in our second loop, we avoid duplicate
# assortments of lengths, like [3, 2], or [2, 1].
for x in range(1, n // 2 + 1):
    for y in range(x, n - x):
        # once we have some appropriate lengths, we need to generate appropriate
        # numbers. We do this by first generating a list of the nums to fill
        # and then passing it to a recursive function.
        nums = list(range(1, n + 1))
        # we add our results to the end of any previous results, and continue
        answer.extend(checkPandigital(x, "", y, "", nums))

# we then need to filter out duplicate products, by transferring to another arr
res = []
[res.append(x) for x in answer if x not in res]
# finally we sum all our products and print
print(sum(res))




