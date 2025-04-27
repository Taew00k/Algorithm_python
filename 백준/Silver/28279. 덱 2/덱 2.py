from collections import deque
import sys
input = sys.stdin.readline
list = deque()


N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == '1':
        list.appendleft(order[1])
    elif order[0] == '2':
        list.append(order[1])
    elif order[0] == '3':
        if len(list)>0:
            print(list.popleft())
        else:
            print(-1)
    elif order[0] == '4':
        if len(list)>0:
            print(list.pop())
        else:
            print(-1)
    elif order[0] == '5':
        print(len(list))
    elif order[0] == '6':
        if len(list)>0:
            print(0)
        else:
            print(1)
    elif order[0] == '7':
        if len(list)>0:
            print(list[0])
        else:
            print(-1)
    elif order[0] == '8':
        if len(list)>0:
            print(list[-1])
        else:
            print(-1)