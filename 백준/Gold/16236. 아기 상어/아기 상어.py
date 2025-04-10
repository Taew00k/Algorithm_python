from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어 초기 상태
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j  # 상어 위치
            graph[i][j] = 0  # 시작 위치 비우기

size = 2  # 상어 크기
ate = 0   # 지금까지 먹은 수
time = 0  # 총 시간

def bfs(x, y, size):
    visited = [[-1]*n for _ in range(n)]
    visited[x][y] = 0
    q = deque()
    q.append((x, y))
    fishes = []

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] <= size:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))
                    if 0 < graph[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))  # 거리, x, y

    # 정렬 조건: 거리 → 위쪽 → 왼쪽
    fishes.sort()
    return fishes

while True:
    fish_list = bfs(sx, sy, size)
    if not fish_list:
        break
    dist, fx, fy = fish_list[0]
    time += dist
    ate += 1
    graph[fx][fy] = 0
    sx, sy = fx, fy
    if ate == size:
        size += 1
        ate = 0

print(time)
