n, m = map(int, input().split())
check_list = []
count = 0

for _ in range(n):
    check_list.append(input())

check_list_set = set(check_list)

for _ in range(m):
    need_check = input()
    if need_check in check_list_set:
        count += 1

print(count)