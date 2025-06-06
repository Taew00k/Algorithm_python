from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
y = max(map(max, graph))
answer = 1

def bfs(a,b,height):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        n,m = queue.popleft()
        for num in range(4):
            nx = n + dx[num]
            ny = m + dy[num]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

for k in range(0,y+1):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                count += 1
    answer = max(answer, count)

print(answer)