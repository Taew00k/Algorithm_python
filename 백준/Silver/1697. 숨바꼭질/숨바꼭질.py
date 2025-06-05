from collections import deque
n,k = map(int, input().split())
visited = [-1] * 100001

def bfs(x):
    queue = deque()
    visited[x]= 0
    queue.append(x)

    while queue:
        a = queue.popleft()
        if a == k:
            return visited[a]
        for i in [a-1, a+1, 2*a]:
            if 0<=i<=100000 and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[a] + 1

print(bfs(n))