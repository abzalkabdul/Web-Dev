if __name__ == '__main__':
    arr=sorted([int(input()) for _ in range(int(input()))])
    for num in arr[::-1]:
        if arr[-1] != num:
            print(num)
            break
