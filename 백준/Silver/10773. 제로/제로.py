import sys
input = sys.stdin.readline
num_list = []

k = int(input())
for _ in range(k):
    number = int(input())
    if number == 0:
        num_list.pop()
    else:
        num_list.append(number)

print(sum(num_list))