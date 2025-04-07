from collections import deque

N = int(input())
graph = []
count_list = []
total_count = 0

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count+=1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count_list.append(bfs(i,j))

print(len(count_list))
for i in sorted(count_list):
    print(i)