from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1

    while queue:
        a = queue.popleft()
        for i in range(1, n+1):
            if visited[i] == 0 and graph[a][i] and graph[i][a]:
                queue.append(i)
                visited[i] = visited[a] + 1
                if i == p2:
                    return visited[i] - 1
    return -1

print(bfs(p1))