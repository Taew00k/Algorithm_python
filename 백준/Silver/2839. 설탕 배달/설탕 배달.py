n = int(input())
count = 0
number = n

while True:
    number -= 5
    count += 1
    if number < 5:
        break

while True:
    if number % 3 == 0:
        count += number // 3
        break
    else:
        number += 5
        count -=1
        if number>n:
            print(-1)
            exit()

print(count)