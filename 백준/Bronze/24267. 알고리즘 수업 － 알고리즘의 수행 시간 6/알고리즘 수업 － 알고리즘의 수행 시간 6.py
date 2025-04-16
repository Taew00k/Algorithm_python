n = int(input())
count = 1
sum = 0

for i in range(n-2, 0, -1):
    sum += i * count
    count += 1

print(sum)
print(3)