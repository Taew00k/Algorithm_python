M = int(input())
N = int(input())
total= 0
min_num = 0

for i in range(M,N+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
            if count > 2:
                break
    if count == 2:
        if total == 0:
            min_num = i
        total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_num)
