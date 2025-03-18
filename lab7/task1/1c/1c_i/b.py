a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(*[x for x in range(a,b) if x%d==c])