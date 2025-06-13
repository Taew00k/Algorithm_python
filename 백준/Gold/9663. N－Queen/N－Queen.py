n = int(input())
count = 0

cols = set()
pos_diagonals = set()
neg_diagonals = set() 

def chess(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
            continue

        cols.add(col)
        pos_diagonals.add(row + col)
        neg_diagonals.add(row - col)

        chess(row + 1)

        cols.remove(col)
        pos_diagonals.remove(row + col)
        neg_diagonals.remove(row - col)

chess(0)
print(count)
