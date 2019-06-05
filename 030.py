# very simple

n = int(input())
totalSum = 0
# go through every number 10-1000000
# probably a lower limit possible, but going through and finding upper limit
# manually would require finding the numbers, which means I could just save
# the sums anyway so whatever
for i in range(10, 1000000):
    # take powers of each digit in each number and compare to original number
    val = 0
    temp = i
    while temp > 0:
        val += (temp % 10) ** n
        temp = temp // 10
    # if they are equal, add to saved total, then print at end
    if val == i:
        totalSum += val
print(totalSum)
