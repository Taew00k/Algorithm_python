from collections import defaultdict

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    for result in results:
        graph[result[0]].append((1, result[1]))
        graph[result[1]].append((0, result[0]))
    for i in range(1, n+1):
        for k in graph[i]:
            win, idx = k
            for x in graph[idx]:
                if x[0] == win and x not in graph[i]:
                    graph[i].append(x)
    for g in range(1, n+1):
        if len(graph[g]) == n-1:
            answer += 1
            
    return answer