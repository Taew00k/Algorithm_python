n,m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input())))
white_board = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]

min_paint = 64

for i in range(n-7):
    for j in range(m-7):
        count = 0

        for row in range(8):
            for col in range(8):
                if board[row+i][col+j] != white_board[row][col]:
                    count += 1

        min_paint = min(min_paint, count, 64-count)

print(min_paint)