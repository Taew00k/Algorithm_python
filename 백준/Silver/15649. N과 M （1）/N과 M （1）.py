from itertools import permutations
n,m = map(int, input().split())
num_list = []

for i in range(1,n+1):
    num_list.append(i)

combi = list(permutations(num_list, m))

for j in range(len(combi)):
    for k in range(m):
        print(combi[j][k], end=" ")
    print()