import sys
sys.setrecursionlimit(200000) 

n, m, r = map(int, input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global count
    count += 1
    visited[x] = count
    graph[x].sort()
    for j in graph[x]:
        if not visited[j]:
            dfs(j)

dfs(r)

for i in range(1, n+1):
    print(visited[i])