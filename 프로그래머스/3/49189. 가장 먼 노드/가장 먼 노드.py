from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited = [0] * (n+1)
    queue = deque()
    
    def find_graph(x):
        queue.append(x)
        visited[x] = 1
        count = 1
        while queue:
            if count == n:
                break
            a = queue.popleft()
            count += 1
            for i in graph[a]:
                if not visited[i]:
                    visited[i] = visited[a] + 1
                    queue.append(i)
    find_graph(1)
    for visit in visited:
        if visit == max(visited):
            answer += 1
    return answer 