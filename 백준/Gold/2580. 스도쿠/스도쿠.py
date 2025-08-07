graph = []
for _ in range(9):
    graph.append(list(map(int, input().split())))

empty = []  # 0인 위치를 미리 저장

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))

def find_col(row):
    num_list = {1,2,3,4,5,6,7,8,9}
    for k in range(9):
        if graph[row][k] != 0:
            num_list.discard(graph[row][k])
    return num_list

def find_row(col):
    num_list = {1,2,3,4,5,6,7,8,9}
    for k in range(9):
        if graph[k][col] != 0:
            num_list.discard(graph[k][col])
    return num_list

def find_square(row, col):
    num_list = {1,2,3,4,5,6,7,8,9}
    for x in range(row//3*3, row//3*3+3):
        for y in range(col//3*3, col//3*3+3):
            if graph[x][y] != 0:
                num_list.discard(graph[x][y])
    return num_list

def dfs(idx):
    if idx == len(empty):
        for row in graph:
            print(' '.join(map(str, row)))
        exit(0)
    i, j = empty[idx]
    possible = find_col(i) & find_row(j) & find_square(i, j)
    for num in possible:
        graph[i][j] = num
        dfs(idx+1)
        graph[i][j] = 0

dfs(0)