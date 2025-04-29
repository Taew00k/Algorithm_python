import sys
input = sys.stdin.readline

N = int(input())
num_list = []
array = [0] * 8001
for _ in range(N):
    k = int(input())
    num_list.append(k)
    array[k+4000] += 1
num_list.sort()
result = []
for i in range(len(array)):
    if array[i]>0:
        result.append([-array[i], i-4000])
result.sort()

print(round(sum(num_list)/N))
print(num_list[N//2])
if len(result)>1 and result[0][0] == result[1][0]:
    print(result[1][1])
else:
    print(result[0][1])
print(num_list[-1]-num_list[0])