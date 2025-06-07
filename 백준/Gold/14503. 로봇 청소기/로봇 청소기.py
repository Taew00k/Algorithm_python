N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean_room():
    x, y, direction = r, c, d
    count = 0
    
    while True:
        if graph[x][y] == 0:
            graph[x][y] = 2
            count += 1
        
        cleaned = False
        for _ in range(4):
            direction = (direction - 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                x, y = nx, ny
                cleaned = True
                break

        if not cleaned:
            back_direction = (direction + 2) % 4
            nx = x + dx[back_direction]
            ny = y + dy[back_direction]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
                x, y = nx, ny
            else:
                break
    
    return count

print(clean_room())