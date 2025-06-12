N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
used = [False] * 9
lineup = [0] * 9

def simulate_game():
    global max_score
    score = 0
    idx = 0

    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            result = inning[lineup[idx]]
            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif result == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    max_score = max(max_score, score)

def make_lineup(depth):
    if depth == 9:
        if lineup[3] == 0:
            simulate_game()
        return

    for i in range(9):
        if not used[i]:
            used[i] = True
            lineup[depth] = i
            make_lineup(depth + 1)
            used[i] = False

make_lineup(0)
print(max_score)
