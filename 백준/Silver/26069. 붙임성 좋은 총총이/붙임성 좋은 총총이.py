n = int(input())
people = set()

for _ in range(n):
    a,b = input().split()
    if a == "ChongChong" or b == "ChongChong":
        people.add(a)
        people.add(b)
    elif a in people or b in people:
        people.add(a)
        people.add(b)

print(len(people))