n = int(input())
num_list = []
dp = []
for j in range(n):
    num_list.append(list(map(int, input().split())))
    dp.append([0] * (j+1))

dp[0][0] = num_list[0][0]

for i in range(n-1):
    for k in range(i+1):
        if dp[i+1][k] < num_list[i+1][k] + dp[i][k]:
            dp[i+1][k] = num_list[i+1][k] + dp[i][k]
        if dp[i+1][k+1] < num_list[i+1][k+1] + dp[i][k]:
            dp[i+1][k+1] =  num_list[i+1][k+1] + dp[i][k]

print(max(dp[n-1]))