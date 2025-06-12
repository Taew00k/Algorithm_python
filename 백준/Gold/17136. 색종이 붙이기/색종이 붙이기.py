board = [list(map(int, input().split())) for _ in range(10)]
paper_count = [0] * 6
min_total = 99999

def can_attach(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if board[x + i][y + j] != 1:
                return False
    return True

def attach(x, y, size, value):
    for i in range(size):
        for j in range(size):
            board[x + i][y + j] = value

def dfs(pos, used):
    global min_total

    if pos == 100:
        min_total = min(min_total, used)
        return

    x = pos // 10
    y = pos % 10

    if board[x][y] == 0:
        dfs(pos + 1, used)
        return

    for size in range(5, 0, -1):
        if paper_count[size] >= 5:
            continue
        if can_attach(x, y, size):
            attach(x, y, size, 0)
            paper_count[size] += 1
            dfs(pos + 1, used + 1)
            paper_count[size] -= 1
            attach(x, y, size, 1)

def solve():
    dfs(0, 0)
    print(min_total if min_total != 99999 else -1)

solve()