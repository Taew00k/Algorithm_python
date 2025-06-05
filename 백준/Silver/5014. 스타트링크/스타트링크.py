from collections import deque
F,S,G,U,D = map(int, input().split())
visited = [-1] * (F+1)

def bfs(x):
    visited[x] = 0
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        if a == G:
            return visited[a]
        if 1 <= a + U <= F and visited[a+U] == -1:
            queue.append(a+U)
            visited[a+U] = visited[a] + 1
        if 1 <= a - D <= F and visited[a-D] == -1:
            queue.append(a-D)
            visited[a-D] = visited[a] + 1
    return 'use the stairs'

print(bfs(S))


