num = int(input())
total, t = 0, 1
while t < num:
    if (t**0.5).is_integer():
        print(t)
        total +=t
    t+=1