N = int(input())

for i in range(1, N+1):
    total = i
    string = str(i)
    length = len(string)
    for j in range(length):
        total += int(string[j])
    if total == N:
        print(i)
        exit()
print(0)
