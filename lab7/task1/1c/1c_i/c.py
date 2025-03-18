a, b = int(input()), int(input())
print(*[x for x in range(a,b) if (x**0.5).is_integer()])