n = int(input())
have_card = list(map(int, input().split()))
have_card_set = set(have_card)
k = int(input())
check_card = list(map(int, input().split()))

for i in range(k):
    if check_card[i] in have_card_set:
        print(1, end=" ")
    else:
        print(0, end=" ")