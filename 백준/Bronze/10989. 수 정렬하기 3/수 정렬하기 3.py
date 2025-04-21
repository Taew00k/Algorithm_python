import sys
input = sys.stdin.readline

n = int(input())
num_list = [0] * 10001

for _ in range(n):
    num = int(input())
    num_list[num] += 1

for i in range(10001):
    for k in range(num_list[i]):
        print(i)
