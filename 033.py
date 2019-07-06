def cancelNum(ratio, numerator, denominator, k):
    #print("n: " + str(numerator) + " d: " + str(denominator) + " k: " + str(k))
    numlist = [int(d) for d in str(numerator)]
    denlist = [int(d) for d in str(denominator)]
    #print("nl: ")
    #print(numlist)
    #print("dl: ")
    #print(denlist)
    if (len(numlist) == 1 or len(denlist) == 1):
        return [0, 0]
    numlistIter = numlist.copy()
    numlistIter.sort()
    for num in numlistIter:
        if num != 0 and num in denlist:
            if k == 1:
                numlistcopy = numlist.copy()
                numlistcopy.remove(num)
                numcopy = int(''.join(map(str,numlistcopy)))
                denlistcopy = denlist.copy()
                denlistcopy.remove(num)
                dencopy = int(''.join(map(str,denlistcopy)))
                if dencopy != 0 and ratio == numcopy / dencopy:
                    #print("(" + str(numerator) + ", " + str(denominator) + ", " + str(numcopy) + ", " + str(dencopy) + ")")
                    return [numerator, denominator]
            else:
                numlistcopy = numlist.copy()
                numlistcopy.remove(num)
                numcopy = int(''.join(map(str,numlistcopy)))
                denlistcopy = denlist.copy()
                denlistcopy.remove(num)
                dencopy = int(''.join(map(str,denlistcopy)))
                if (cancelNum(ratio, numcopy, dencopy, k - 1) != [0, 0]):
                    #print("(" + str(numerator) + ", " + str(denominator) + ", " + str(numcopy) + ", " + str(dencopy) + ")")
                    return [numerator, denominator]
                else:
                    return [0, 0]
    return [0, 0]




temp = str(input())
n = int(temp[0])
k = int(temp[2])
numsum = 0
densum = 0

for x in range(10 ** (n - 1), 10 ** n):
    for y in range(x + 1, 10 ** n):
        print("x: " + str(x) + " y: " + str(y))
        res = cancelNum(x/y, x, y, k)
        numsum += res[0]
        densum += res[1]

print(str(numsum) + " " + str(densum))
