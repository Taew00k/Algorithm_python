num_list = []
for _ in range(5):
    num_list.append(int(input()))

num_list.sort()
total = sum(num_list) // 5
print(total)
print(num_list[2])