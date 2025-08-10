N = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for index in range(3,N+1):
    dp[index] = (dp[index-2] + dp[index-1]) % 15746

print(dp[N])
