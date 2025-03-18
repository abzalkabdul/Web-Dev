def minimum(a,b,c,d):
    lst=[a,b,c,d]
    mnm=lst[0]
    for i in range(len(lst)):
        if mnm > lst[i]:
            mnm = lst[i]
    return mnm

print(minimum(5,4,6,7))