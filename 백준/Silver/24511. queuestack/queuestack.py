N = int(input())
queuestack = list(map(int, input().split()))
value = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
answer = []

for i in range(N-1,-1, -1):
    if queuestack[i] == 0:
        answer.append(value[i])
        
for j in range(M):
    answer.append(C[j])

for k in range(M):
    print(answer[k], end=" ")