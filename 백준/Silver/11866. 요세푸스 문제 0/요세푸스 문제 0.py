from collections import deque
n, k = map(int, input().split())
queue = deque()
result = []

for i in range(1,n+1):
    queue.append(i)

while True:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
    if not queue:
        break

print("<", end="")
for i in range(len(result)):
    print(result[i], end="")
    if not i == len(result) -1:
        print(", ", end="")
print(">", end="")