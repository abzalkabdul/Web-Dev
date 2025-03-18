#1
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (is_weekend or cigars <= 60)

#2
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

#3
def squirrel_play(temperature, is_summer):
    upper_limit = 100 if is_summer else 90
    return 60 <= temperature <= upper_limit

#4
def sorta_sum(a, b):
    total = a + b
    return 20 if 10 <= total <= 19 else total

#5
def alarm_clock(day, vacation):
    if vacation:
        return "10:00" if 1 <= day <= 5 else "off"
    return "7:00" if 1 <= day <= 5 else "10:00"

#6
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

#7
def in1to10(n, outside_mode):
    return (1 <= n <= 10) if not outside_mode else (n <= 1 or n >= 10)

#8
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
