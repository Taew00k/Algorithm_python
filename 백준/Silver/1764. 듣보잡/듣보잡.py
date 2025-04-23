n,m = map(int, input().split())
no_hear = set()
no_watch = set()
for _ in range(n):
    no_hear.add(input())
for _ in range(m):
    no_watch.add(input())

answer = list(no_hear & no_watch)
answer.sort()

print(len(answer))
for i in range(len(answer)):
    print(answer[i])