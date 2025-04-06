from collections import deque

N,M = map(int, input().split())
graph = []

for _ in range(N):
    miro = list(map(int, input()))
    graph.append(miro)

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            dx = a + move_x[i]
            dy = b + move_y[i]
            if 0<=dx<N and 0<=dy<M and graph[dx][dy]==1:
                queue.append((dx,dy))
                graph[dx][dy] = graph[a][b] + 1
    return graph[N-1][M-1]

print(bfs(0,0))