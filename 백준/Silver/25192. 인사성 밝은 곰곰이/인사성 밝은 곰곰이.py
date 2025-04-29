n = int(input())
count = 0
chat = set()
for _ in range(n):
    k = input()
    if k == "ENTER":
        count += len(chat)
        chat = set()
    else:
        chat.add(k)
count += len(chat)
print(count)