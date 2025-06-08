from collections import deque
n,m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer_count = 0

def year_ago():
    copy_ice = [row[:] for row in ice]
    result = 0
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0:
                count = 0
                for a in range(4):
                    nx = i + dx[a]
                    ny = j + dy[a]
                    if 0<=nx<n and 0<=ny<m and ice[nx][ny] == 0:
                        count += 1
                if ice[i][j] - count <= 0:
                    copy_ice[i][j] = 0
                else:
                    copy_ice[i][j] -= count
                    result += 1
    return copy_ice, n*m-result

def bfs(x):
    have_number = set()
    visited = [[0] * m for _ in range(n)]
    field = x
    queue = deque()
    for i in range(n):
        for j in range(m):
            if field[i][j] !=0:
                have_number.add((i,j))
    queue.append(have_number.pop())
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != 0 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                have_number.discard((nx,ny))
                visited[nx][ny] = 1
    if len(have_number) == 0:
        return False
    else:
        return True

while True:
    ice, num = year_ago()
    if num == n*m:
        print(0)
        exit()
    isTrue = bfs(ice)
    answer_count+=1
    if isTrue:
        print(answer_count)
        exit()