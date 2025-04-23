n = int(input())
people = set()

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        people.add(name)
    elif status == 'leave':
        people.remove(name)

people_list = list(people)
people_list.sort()

for i in range(len(people_list)-1,-1,-1):
    print(people_list[i])