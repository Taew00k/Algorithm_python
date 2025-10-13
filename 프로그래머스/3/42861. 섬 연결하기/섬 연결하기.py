from collections import defaultdict
import heapq

def solution(n, costs):
    graph = defaultdict(list)
    for cost in costs:
        graph[cost[0]].append((cost[2], cost[1]))
        graph[cost[1]].append((cost[2], cost[0]))
    for k,v in graph.items():
        v.sort(key = lambda x: x[0])
    visited = [False] * n
    min_cost = 0
    heap = [(0,0)]

    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        min_cost += cost
        
        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_cost, next_node))
    
    return min_cost
        
        
        
        