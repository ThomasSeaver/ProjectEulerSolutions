# pre-calculate factorials. Probably unnecessary, but why not
fact = [1] * 10

for i in range(1, 10):
    fact[i] = i * fact[i - 1]


# take in input
n = int(input())
total = 0
for i in range(10, n):
    # for each digit 10 -> n, break into individual digits
    digits = [int(d) for d in str(i)]
    summation = 0
    # sum up factorials of every digit
    for digit in digits:
        summation += fact[digit]
    # if sum is divisible by original number, add to total and print
    if summation % i == 0:
        total += i
print(total)

