n = int(input())
number = 1
j = 1
count = 0

while True:
    if j**2 > n:
        break
    count+=1
    j+=1

print(count)
