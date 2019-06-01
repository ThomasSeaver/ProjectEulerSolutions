def toNum(s):
    finalStr = ""
    s = int(s)
    if s == 0:
        finalStr = "Zero"
    elif s == 1:
        finalStr = "One"
    elif s == 2:
        finalStr = "Two"
    elif s == 3:
        finalStr = "Three"
    elif s == 4:
        finalStr = "Four"
    elif s == 5:
        finalStr = "Five"
    elif s == 6:
        finalStr = "Six"
    elif s == 7:
        finalStr = "Seven"
    elif s == 8:
        finalStr = "Eight"
    elif s == 9:
        finalStr = "Nine"
    elif s == 10:
        finalStr = "Ten"
    elif s == 11:
        finalStr = "Eleven"
    elif s == 12:
        finalStr = "Twelve"
    elif s == 13:
        finalStr = "Thirteen"
    elif s == 14:
        finalStr = "Fourteen"
    elif s == 15:
        finalStr = "Fifteen"
    elif s == 16:
        finalStr = "Sixteen"
    elif s == 17:
        finalStr = "Seventeen"
    elif s == 18:
        finalStr = "Eighteen"
    elif s == 19:
        finalStr = "Nineteen"
    else:
        t = int(str(s)[:1])
        q = int(str(s)[1:])
        if t == 2:
            finalStr = "Twenty"
        if t == 3:
            finalStr = "Thirty"
        if t == 4:
            finalStr = "Forty"
        if t == 5:
            finalStr = "Fifty"
        if t == 6:
            finalStr = "Sixty"
        if t == 7:
            finalStr = "Seventy"
        if t == 8:
            finalStr = "Eighty"
        if t == 9:
            finalStr = "Ninety"
        if q != 0:
            finalStr += " " + toNum(q)
    return finalStr



def parse(s, count):
    finalStr = ""
    added = ""
    if int(s) != 0:
        if (count == 1):
            added = " Thousand"
        elif (count == 2):
            added = " Million"
        elif (count == 3):
            added = " Billion"
        elif (count == 4):
            added = " Trillion"
        if len(s) == 3 and int(s[:1]) != 0:
            finalStr += toNum(s[:1]) + " Hundred"
            if int(s[-2:]) != 0:
                finalStr += " "
        if int(s[-2:]) != 0:
            finalStr += toNum(str(s)[-2:])
        finalStr += added + " "
    return finalStr


t = int(input())
for i in range(t):
    n = str(input())
    count = 0
    parsed = ""
    while len(n) > 0:
        s = n[-3:]
        parsed = parse(s, count) + parsed
        count += 1
        n = n[:-3]
    print(parsed)