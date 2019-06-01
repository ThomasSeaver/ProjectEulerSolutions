txt = input()
result = 0
for x in range(int(txt)):
    temp = input()
    result = result + int(temp)

print(str(result)[:10])