N = int(input())
word_list = {}
word_name = []

for _ in range(N):
    a,b = input().split('.')
    if b in word_list:
        word_list[b] += 1
    else:
        word_list[b] = 1
        word_name.append(b)
word_name.sort()

for i in word_name:
    print(i, word_list[i])