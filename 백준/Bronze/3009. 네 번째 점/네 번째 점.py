spot = []

for _ in range(3):
    spot.append(list(map(int, input().split())))

if spot[0][0] == spot[1][0]:
    new_x = spot[2][0]
elif spot[0][0] == spot[2][0]:
    new_x = spot[1][0]
else:
    new_x = spot[0][0]

if spot[0][1] == spot[1][1]:
    new_y = spot[2][1]
elif spot[1][1] == spot[2][1]:
    new_y = spot[0][1]
else:
    new_y = spot[1][1]

print(f'{new_x} {new_y}')
