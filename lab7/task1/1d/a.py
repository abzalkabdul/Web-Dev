lst = [int(input()) for _ in range(int(input()))]
print(*[lst[i] for i in range(len(lst)) if i%2==0])