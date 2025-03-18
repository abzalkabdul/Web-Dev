n = int(input())
while n > 1 and n%2 == 0:
    n //=2
print('YES' if n==1 else "NO")