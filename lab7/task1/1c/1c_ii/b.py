num = int(input())
x = 1
min = 0
while x<num:
    if num%x==0 and x!=1:
        min=x
        print(min)
        break
    x+=1