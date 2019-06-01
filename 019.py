import math

# for each test case
t = int(input())
for n in range(t):
    # instantiate our date lists
    sunCount = 0
    dateA = list(map(int, list(input().split())))
    # if our day is not zero, we don't want to check this month
    # jump a month forward, and check if it pushes us to next year
    if dateA[2] != 1:
        dateA[1] += 1
        if dateA[1] == 13:
            dateA[1] = 1
            dateA[0] += 1
        dateA[2] = 1
    dateB = list(map(int, list(input().split())))
    # if our end date is not the first of the month, push it so it is
    if dateB[2] != 1:
        dateB[2] = 1
    # also because our while loop ends when we reach our end date, push
    # our end date back a month. Check if our year has to increment,
    # similar to above.
    dateB[1] += 1
    if dateB[1] == 13:
        dateB[1] = 1
        dateB[0] += 1

    # set our year and month variables to our first date
    year = dateA[0]
    month = dateA[1]

    # Zeller Congruence Calculation
    # formula treats jan/feb as 13/14 of last year, so check if these need
    # to be moved from standard date to appropriate values
    if (month < 3):
        month += 12
        year -= 1
    # get formula bits
    K = year % 100
    J = year // 100
    # actual formula, modified from -2J to +5J so modulus stays positive
    weekDay = (1 + math.floor(13 * (month + 1) / 5) + K + math.floor(K/4) + math.floor(J/4) + (5 * J)) % 7
    # if we modified our date from above, unmodify
    if (month > 12):
        month -= 12
        year += 1

    # until we reach our end date
    while (month != dateB[1] or year != dateB[0]):
        # check current day
        if weekDay == 1:
            sunCount += 1
        # if february and a leap year, add 1 to our count
        # since 29 % 7 is 1, weekday of march 1 will be 1 later than weekday
        # of feb 1
        if month == 2:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                weekDay += 1
            # if not leap year, march 1 same as feb 1
        # for months with 30 days, add two since 30 % 7 is 2
        elif month == 4 or month == 6 or month == 9 or month == 11:
            weekDay += 2
        # and for 31 days, add 3
        else:
            weekDay += 3
        # modulus our count, increment our month, check if our year needs to
        # be ticked over
        weekDay = weekDay % 7
        month += 1
        if month == 13:
            month = 1
            year += 1

    # finally we have our count
    print(sunCount)



