from itertools import combinations
graph = []
n,m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append([i,j])

answer = 1e9
for combi in combinations(chicken, m):
    total = 0
    for h in house:
        dist = min(abs(h[0]-c[0]) + abs(h[1]-c[1]) for c in combi)
        total += dist
    answer = min(answer, total)
    
print(answer)