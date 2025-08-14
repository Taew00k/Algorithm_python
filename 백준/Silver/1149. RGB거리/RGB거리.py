N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N)]
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]

for i in range(1,N):
    dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = house[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = house[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))