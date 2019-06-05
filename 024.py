# this is some fancy math stuff that is pretty confusing but here's a wikipedia
# https://en.wikipedia.org/wiki/Factorial_number_system#Permutations
# the example showing factoradic -> permuation is analagous, and helpful
# the main first part demonstrates building factoradics, and what they are
import math


# for each test case
t = int(input())
for _ in range(t):
    # take in n'th permutation but index from 0
    n = int(input()) - 1
    alphabet = "abcdefghijklm"

    # build factoradic
    # divide by an increasing number, and add remainder to list to build
    # skip one, as n / 1 = 1 and n % 1 = 0
    factoradic = [0]
    for i in range(2, 14):
        factoradic.insert(0, str(n % i))
        n = math.floor(n / i)

    # build permutation
    # take each modulus remainder from our factoradic, and use that as an index
    # to pull a character out of our alphabet and build the n'th permutation
    permutation = ""
    for j in range(13):
        place = int(factoradic[j])
        permutation += alphabet[place]
        alphabet = alphabet[:place] + alphabet[place+1:]

    print(permutation)
