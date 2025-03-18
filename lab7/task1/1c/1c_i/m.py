x = int(input())
lst=[int(input()) for _ in range(x)]
cnt=0
for num in lst:
    for n in num:
        if n=="0":
            cnt+=1
print(cnt)
