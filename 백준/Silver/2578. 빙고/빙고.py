bingo = []
num_list = []
count = 0
visited = [[0] * 5 for _ in range(5)]
check = True

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    num_list.append(list(map(int, input().split())))

def find_bing(call):
    global count
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == call:
                visited[x][y] = 1
                count += 1

def check_bing():
    line = 0
    lcross_cnt = 0
    rcross_cnt = 0

    for x in range(5):
        x_cnt = 0
        y_cnt = 0
        for y in range(5):
            if visited[x][y] == 1:
                x_cnt += 1
            if visited[y][x] == 1:
                y_cnt += 1
            if x + y == 4 and visited[x][y] == 1:
                lcross_cnt += 1
            if x == y and visited[x][y] == 1:
                rcross_cnt +=1
            if x_cnt == 5:
                line += 1
            if y_cnt == 5:
                line += 1
    if lcross_cnt == 5:
        line += 1
    if rcross_cnt == 5:
        line += 1
    return line

for i in range(5):
    for j in range(5):
        num = num_list[i][j]
        find_bing(num)
        if check_bing() >= 3:
            print(count)
            exit()