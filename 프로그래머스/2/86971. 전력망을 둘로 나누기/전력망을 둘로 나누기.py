from collections import defaultdict, deque

def dfs(graph, visited, start):
    count = 1
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for wire in graph[x]:
            if not visited[wire]:
                queue.append(wire)
                visited[wire] = 1
                count += 1
    return count
            

    
    
def solution(n, wires):
    min_result = n
    for i in range(n):
        new_wire = wires[:i] + wires[i+1:]
        visited = [0] * (n+1)
        graph = defaultdict(list)
        for wire in new_wire:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
        result = abs(n - 2 * dfs(graph, visited, 1))
        min_result = min(min_result, result)
    return min_result
        