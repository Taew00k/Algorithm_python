import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)