from collections import defaultdict, deque

def bfs(n, start, graph, visited):
    count = 0
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:
                queue.append(y)
                count += 1
                visited[y] = 1
    return count
    

def solution(n, computers):
    visited = [0] * n
    answer = 0
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    for k in range(n):
        if not visited[k]:
            answer += bfs(n, k, graph,visited)
    return n - answer
    
    