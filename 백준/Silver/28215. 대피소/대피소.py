from itertools import combinations
n,k = map(int, input().split())
house_list = []
for _ in range(n):
    house_list.append(list(map(int, input().split())))

house_combination = list(combinations(house_list, k))
dist = 1e9
for combi in house_combination:
    dis_list = []
    for house in house_list:
        less_dist = 1e9
        for c in combi:
            distance = abs(c[0]-house[0]) + abs(c[1] - house[1])
            less_dist = min(less_dist, distance)
        dis_list.append(less_dist)
    dist = min(dist, max(dis_list))
    
print(dist)