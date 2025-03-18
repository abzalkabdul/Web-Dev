def is_leap(year):
    leap = False

    if (leap % 4 == 0 and leap % 1000 != 0) or leap % 400 == 0:
        return True
    return leap


year = int(input())
print(is_leap(year))
