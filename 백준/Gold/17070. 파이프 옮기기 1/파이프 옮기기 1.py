N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if graph[i][j] == 1:
            continue

        # 가로 → 가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]

        # 세로 → 세로
        if i > 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

        # 대각선
        if i > 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))