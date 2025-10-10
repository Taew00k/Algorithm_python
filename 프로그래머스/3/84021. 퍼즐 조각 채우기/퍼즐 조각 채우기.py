from collections import deque

def bfs(board, visited, lst, length, num):
    if board[lst[0]][lst[1]] != num or visited[lst[0]][lst[1]] == 1:
        return
    result = []
    visited[lst[0]][lst[1]] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append(lst)
    while queue:
        x,y = queue.popleft()
        result.append((x,y))
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<length and 0<=ny<length and visited[nx][ny] == 0 and board[nx][ny] == num:
                visited[nx][ny] = 1
                queue.append((nx,ny))
    return result

def make_table(block):
    x = [i[0] for i in block]
    y = [i[1] for i in block]
    
    r = max(y) - min(y) + 1
    c = max(x) - min(x) + 1
    temp = [[0] * r for _ in range(c)]
    
    for i,j in block:
        temp[i-min(x)][j-min(y)] = 1
    return temp
        
def rotate(block):
    count = 0
    r,c = len(block), len(block[0])
    temp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if block[i][j] == 1: 
                count += 1
                temp[j][r-1-i] = block[i][j]
    return temp, count
    
def solution(game_board, table):
    length = len(game_board)
    visited_g = [[0] * length for _ in range(length)]
    visited_t = [[0] * length for _ in range(length)]
    find_g = []
    find_t = []
    for i in range(length):
        for j in range(length):
            g_list = bfs(game_board, visited_g, [i,j], length, 0)
            if g_list:
                find_g.append(g_list)
            t_list = bfs(table, visited_t, [i,j] , length, 1)
            if t_list:
                find_t.append(t_list)
                
    answer = 0
    for empty in find_g:
        flag = False
        g_puzzle = make_table(empty)
        
        for t_block in find_t:
            if flag == True: break
            if len(g_puzzle) > len(t_block):
                continue
            t_puzzle = make_table(t_block)
            
            for _ in range(4):
                t_puzzle, cnt = rotate(t_puzzle)
                
                if t_puzzle == g_puzzle:
                    answer += cnt
                    find_t.remove(t_block)
                    flag = True
                    break
    return answer