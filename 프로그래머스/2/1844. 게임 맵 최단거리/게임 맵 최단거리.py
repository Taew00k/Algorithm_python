from collections import deque

def bfs(maps, visited, row, col):
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<col and 0<=ny<row and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                queue.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
    return visited[col-1][row-1]
        
def solution(maps):
    col = len(maps)
    row = len(maps[0])
    visited = [[0] * row for _ in range(col)]
    answer = bfs(maps, visited, row, col)
    if answer == 0:
        return -1
    else:
        return answer
    
    
    
    