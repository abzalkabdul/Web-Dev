num = int(input())
n = 1
prev = 1
while n < num:
    if n%2==0 or n==1:
        print(n, end=' ')
        n *= 2
    else:
        n += 1