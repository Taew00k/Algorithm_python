from collections import deque
balloon = deque()
result = []
n = int(input())
num_list = list(map(int, input().split()))
for i in range(0,n):
    balloon.append([i+1, num_list[i]])

for _ in range(n):
    result.append(balloon[0][0])
    k = balloon[0][1]
    balloon.popleft()
    if len(balloon) == 0:
        break
    if k>0:
        for _ in range(k-1):
            balloon.append(balloon.popleft())
    elif k<0:
        for _ in range(-k):
            balloon.appendleft(balloon.pop())

for i in result:
    print(i, end=" ")