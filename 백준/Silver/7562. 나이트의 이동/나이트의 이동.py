from collections import deque
case = int(input())
queue = deque()

def bfs(x,y,length):
    visited[x][y] = 1
    queue.append([x,y])
    dx = [2,2,1,1,-1,-1,-2,-2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    while queue:
        a = queue.popleft()
        for i in range(8):
            nx = a[0] + dx[i]
            ny = a[1] + dy[i]
            if 0<=nx<length and 0<=ny<length and visited[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny] = visited[a[0]][a[1]] + 1

for _ in range(case):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    bfs(start_x, start_y, l)
    print(visited[end_x][end_y] - 1)
