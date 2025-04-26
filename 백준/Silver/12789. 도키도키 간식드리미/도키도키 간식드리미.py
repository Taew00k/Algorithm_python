n = int(input())
line = list(map(int, input().split()))
stack = []
count = 1

for num in line:
    if num == count:
        count += 1
    else:
        stack.append(num)
    
    while stack and stack[-1] == count:
        stack.pop()
        count += 1

if not stack:
    print("Nice")
else:
    print("Sad")
