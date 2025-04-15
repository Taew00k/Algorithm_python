N = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(len(arr)):
    check = 0
    a = arr[i]
    if not a==1:
        for j in range(1, a+1):
            if a % j == 0:
                check += 1
        if check == 2:
            count += 1

print(count)