from collections import deque
queue = deque()
apple = []
turn = []
N = int(input())
k = int(input())
for _ in range(k):
    apple.append(list(map(int, input().split())))
l = int(input())
for _ in range(l):
    turn.append(list(input().split()))
time_table = []
for t in turn:
    time_table.append(int(t[0]))
    
board = [[0] * (N+1) for _ in range(N+1)]
move = [(-1,0), (0,1), (1,0), (0,-1)]
direc = 1
time = 0
queue.append((1,1))
board[1][1] = 1

while True:
    time += 1
    
    now_x, now_y = queue[-1]
    nx,ny = now_x + move[direc][0], now_y + move[direc][1]
    
    if not (1<=nx<=N and 1<=ny<=N) or board[nx][ny] == 1:
        print(time)
        break
    
    queue.append((nx,ny))
    board[nx][ny] = 1
        
    if [nx,ny] in apple:
        apple.remove([nx,ny])
    else:
        tail_x, tail_y = queue.popleft()
        board[tail_x][tail_y] = 0
    
    if time in time_table:
        for i in range(len(turn)):
            if time == int(turn[i][0]):
                if turn[i][1] == 'D':
                    direc = (direc + 1)%4
                elif turn[i][1] == 'L':
                    direc = (direc - 1)%4