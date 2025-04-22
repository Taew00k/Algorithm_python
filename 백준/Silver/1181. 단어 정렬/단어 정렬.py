n = int(input())
word_list = []

for _ in range(n):
    word = str(input())
    word_len = len(word)
    if [word_len, word] not in word_list:
        word_list.append([word_len, word])

word_list.sort()
for i in range(len(word_list)):
    print(word_list[i][1])