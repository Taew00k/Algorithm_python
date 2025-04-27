n = int(input())
sum = 1
if n == 0:
    print(1)
    exit()

for i in range(1,n+1):
    sum *= i

print(sum)