lst = [int(input()) for _ in range(int(input()))]
print(*list(filter(lambda x: x%2 == 0, lst)))