i = 0
n = int(input())
count = 1
pibo = 0

while True:
    if not n <= 1+6*pibo:
        count+=1
        i+=1
        pibo += i
    else:
        break

print(count)