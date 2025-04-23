n = int(input())
num_list = [0] * 20000001
have_card = list(map(int, input().split()))
for i in have_card:
    num_list[10000000+i] += 1

m = int(input())
check_card = list(map(int, input().split()))

for m in check_card:
    print(num_list[10000000+m], end=" ")