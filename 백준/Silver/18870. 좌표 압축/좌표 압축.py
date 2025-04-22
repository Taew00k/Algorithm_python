n = int(input())
number = list(map(int, input().split()))
num_set= set(number)
num_list = list(num_set)
result = {}

num_list.sort()
for i in range(len(num_list)):
    result[num_list[i]] = i

for j in number:
    print(result[j], end=" ")