n = int(input())
grid = [['*'] * n for _ in range(n)]

def carve(x, y, size):
    if size == 1:
        return
    third = size // 3
    for i in range(x + third, x + 2*third):
        for j in range(y + third, y + 2*third):
            grid[i][j] = ' '
    for dx in range(0, size, third):
        for dy in range(0, size, third):
            carve(x + dx, y + dy, third)

carve(0, 0, n)

for row in grid:
    print(''.join(row))
