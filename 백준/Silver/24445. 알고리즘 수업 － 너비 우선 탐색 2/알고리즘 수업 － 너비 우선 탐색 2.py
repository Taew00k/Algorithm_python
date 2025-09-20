import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
line = [[] for _ in range(n+1)]
visited = [0] * (n+1)
queue = deque()
count = 1

for _ in range(m):
    u,v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

for lin in line:
    lin.sort(reverse=True)

def bfs(num):
    global count
    visited[num] = count
    count += 1
    queue.append(num)
    while queue:
        x = queue.popleft()
        for y in line[x]:
            if visited[y] == 0:
                queue.append(y)
                visited[y] = count
                count += 1

bfs(r)

for i in range(1,n+1):
    print(visited[i])