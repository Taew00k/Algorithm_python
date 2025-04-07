c = int(input())
n = int(input())
graph = [[0]*(c+1) for _ in range(c+1)]
visited = [False] * (c+1)
count = 0

for _ in range(n):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    global count
    visited[v] = 1
    for i in range(1, c+1):
        if not visited[i] ==1 and graph[v][i] ==1 and graph[i][v]==1:
            count+=1
            dfs(i)
    return count

print(dfs(1))