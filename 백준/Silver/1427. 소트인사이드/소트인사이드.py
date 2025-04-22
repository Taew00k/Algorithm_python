number = list(map(int, input()))
number.sort(reverse=True)

for i in range(len(number)):
    print(number[i], end="")