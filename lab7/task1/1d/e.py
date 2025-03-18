lst = [int(input()) for _ in range(int(input()))]

for i in range(len(lst)-1):
    if lst[i] * lst[i+1] > 0:
        print('YES')
        break
else:
    print('NO')
