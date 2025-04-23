answer = set()
s = input()
for k in range(len(s)):
    start = 0
    end = k + 1
    for _ in range(len(s)-k):
        answer.add(s[start:end])
        start += 1
        end += 1

print(len(answer))