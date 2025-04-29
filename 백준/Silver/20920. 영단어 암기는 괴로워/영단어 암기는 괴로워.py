import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dict = {}
result = []

for _ in range(n):
    k = input().rstrip()
    if len(k) >= m:
        if k in dict.keys():
            dict[k] += 1
        else:
            dict[k] = 1

for i in dict:
    result.append([-dict[i], -len(i), i])

result.sort()

for j in result:
    print(j[2])
