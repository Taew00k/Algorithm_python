a,b,c = map(int,input().split())

total = a+b+c
max_num = max(a,b,c)

if max_num >= total - max_num:
    result = 2 * (total-max_num) - 1
else:
    result = total

print(result)