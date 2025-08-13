n = int(input())
num_list = list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = num_list[0]
max_num = dp[1]

for i in range(1, n):
    dp[i+1] = max(num_list[i], dp[i] + num_list[i])
    if dp[i+1] > max_num:
        max_num = dp[i+1]

print(max_num)
