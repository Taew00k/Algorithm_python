import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    a = input().split()
    if a[0] == '1':
        stack.append(int(a[1]))
    elif a[0] == "2":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == "3":
        print(len(stack))
    elif a[0] == "4":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif a[0] == "5":
        if len(stack) > 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)