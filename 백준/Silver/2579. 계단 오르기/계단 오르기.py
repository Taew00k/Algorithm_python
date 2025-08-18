n = int(input())
num_list = [0] * (n+1)
for i in range(1,n+1):
    num_list[i] = (int(input()))

if n<2:
    print(num_list[n])
else:
    dp = [0] * (n+1)
    dp[1] = num_list[1]
    dp[2] = dp[1] + num_list[2]
    for k in range(3,n+1):
        dp[k] = max(dp[k-3] + num_list[k-1] + num_list[k], dp[k-2] + num_list[k])
    print(dp[-1])