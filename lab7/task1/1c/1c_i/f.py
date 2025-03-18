x = int(input())
print(int(''.join([num for num in str(x)][::-1])))