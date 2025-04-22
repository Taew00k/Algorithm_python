n = int(input())
judge_list = []

for i in range(n):
    age, name = input().split()
    judge_list.append([int(age), i, name])

judge_list.sort()

for i in range(n):
    print(judge_list[i][0],judge_list[i][2])