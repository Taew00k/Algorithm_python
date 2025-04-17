n, m = map(int, input().split())
num_list = list((map(int, input().split())))
max_num = 1e9
result = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = num_list[i] + num_list[j] + num_list[k]
            if  0<= m - total < max_num:
                max_num = abs(total - m)
                result = total

print(result)