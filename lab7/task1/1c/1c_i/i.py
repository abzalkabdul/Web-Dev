num = int(input())
print(len([x for x in range(1, num+1) if num%x==0]))