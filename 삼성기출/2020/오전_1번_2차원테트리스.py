k = int(input())
visited = [[0]*10 for _ in range(10)]
count = 0
visit_block = 0

def move_red(t, x):
    if t == 1:
        for i in range(6, 10):
            if visited[x][i]:
                visited[x][i-1] = 1
                return
        visited[x][9] = 1
    elif t == 2:
        for i in range(6, 10):
            if visited[x][i] or visited[x][i-1]:
                visited[x][i-2] = visited[x][i-1] = 1
                return
        visited[x][8] = visited[x][9] = 1
    else:
        for i in range(6, 10):
            if visited[x][i] or visited[x+1][i]:
                visited[x][i-1] = visited[x+1][i-1] = 1
                return
        visited[x][9] = visited[x+1][9] = 1

def move_yellow(t, y):
    if t == 1:
        for i in range(6, 10):
            if visited[i][y]:
                visited[i-1][y] = 1
                return
        visited[9][y] = 1
    elif t == 2:
        for i in range(6, 10):
            if visited[i][y] or visited[i][y+1]:
                visited[i-1][y] = visited[i-1][y+1] = 1
                return
        visited[9][y] = visited[9][y+1] = 1
    else:
        for i in range(6, 10):
            if visited[i][y] or visited[i-1][y]:
                visited[i-2][y] = visited[i-1][y] = 1
                return
        visited[8][y] = visited[9][y] = 1

def check_red():
    global count
    for i in range(9, 5, -1):
        if all(visited[j][i] for j in range(4)):
            count += 1
            for j in range(4):
                visited[j][i] = 0
            for k in range(i-1, -1, -1):
                for j in range(4):
                    visited[j][k+1] = visited[j][k]
            for j in range(4):
                visited[j][0] = 0
            check_red()
            break

def check_yellow():
    global count
    for i in range(9, 5, -1):
        if all(visited[i][j] for j in range(4)):
            count += 1
            for j in range(4):
                visited[i][j] = 0
            for k in range(i-1, -1, -1):
                for j in range(4):
                    visited[k+1][j] = visited[k][j]
            for j in range(4):
                visited[0][j] = 0
            check_yellow()
            break

def over_red():
    for i in range(4, 6):
        if any(visited[j][i] for j in range(4)):
            for _ in range(1):
                for k in range(9, 4, -1):
                    for j in range(4):
                        visited[j][k] = visited[j][k-1]
                for j in range(4):
                    visited[j][4] = 0

def over_yellow():
    for i in range(4, 6):
        if any(visited[i][j] for j in range(4)):
            for _ in range(1):
                for k in range(9, 4, -1):
                    for j in range(4):
                        visited[k][j] = visited[k-1][j]
                for j in range(4):
                    visited[4][j] = 0

for _ in range(k):
    t, x, y = map(int, input().split())
    move_red(t, x)
    move_yellow(t, y)
    check_red()
    check_yellow()
    over_red()
    over_yellow()

for i in range(6, 10):
    for j in range(4):
        if visited[j][i]:
            visit_block += 1

for i in range(6, 10):
    for j in range(4):
        if visited[i][j]:
            visit_block += 1

print(count)
print(visit_block)
