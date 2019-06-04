# name cache
names = []

# take in names, and sort them automagically via python
t = int(input())
for _ in range(t):
    names.append(input())
names.sort()

# take in our test cases
t = int(input())
for _ in range(t):
    # take in our test case, and check through our name cache to get i'th
    # position in sorted list
    name = input()
    i = 0
    while names[i] != name:
        i += 1
    i += 1
    # generate nameScore by using ascii value of characters and converting
    nameScore = 0
    while len(name) > 0:
        nameScore += ord(name[:1]) - 64
        name = name[1:]
    # print result
    print(nameScore * i)


