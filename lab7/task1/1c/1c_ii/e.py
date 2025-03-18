n = int(input())
k, power = 0, 1

while power < n:
    power *= 2
    k += 1
print(k)