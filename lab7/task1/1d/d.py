lst = [int(input()) for _ in range(int(input()))]
cnt=0
for i in range(1,len(lst)):
    if lst[i]>lst[i-1]:
        cnt+=1
print(cnt)
