from collections import deque

m,n,h = map(int, input().split())
graph = []

for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    graph.append(box)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    queue.append((z,y,x))
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz, ny, nx))

bfs()

days = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                print(-1)
                exit()
            days = max(days, graph[z][y][x])

print(days - 1)