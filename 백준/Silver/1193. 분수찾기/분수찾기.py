x = int(input())

total = 1
count = 1

while True:
    if x<= total:
        break
    else:
        count += 1
        total += count

if count % 2 == 0:
    print(f"{count - total + x}/{total - x + 1}")
else:
    print(f"{total-x+1}/{count-total+x}")