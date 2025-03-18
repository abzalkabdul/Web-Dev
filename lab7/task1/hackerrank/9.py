lst = []
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]

    if action == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif action == "print":
        print(lst)
    elif action == "remove":
        lst.remove(int(command[1]))
    elif action == "append":
        lst.append(int(command[1]))
    elif action == "sort":
        lst.sort()
    elif action == "pop":
        lst.pop()
    elif action == "reverse":
        lst.reverse()
