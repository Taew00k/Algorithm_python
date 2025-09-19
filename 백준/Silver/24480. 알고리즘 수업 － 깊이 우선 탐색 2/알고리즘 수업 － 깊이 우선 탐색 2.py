import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
visited = [0] * (n+1)
line = [[] for _ in range(n+1)]
count = 1
for _ in range(m):
    a,b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)

for lst in line:
    lst.sort(reverse=True)

def dfs(num):
    global count
    visited[num] = count
    count += 1
    for i in line[num]:
        if visited[i]:
            continue
        dfs(i)

dfs(r)

for k in range(1, len(visited)):
    print(visited[k])