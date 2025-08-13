dp = [0] * 101
T = int(input())
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for _ in range(T):
    n = int(input())
    if n>4:
        for i in range(5,n+1):
            dp[i] =  dp[i-3] + dp[i-2]
    print(dp[n])
