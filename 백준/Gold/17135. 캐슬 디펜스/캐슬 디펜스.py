n,m,d = map(int, input().split())
original_field = []
arrower = []
max_result = 0
for _ in range(n):
    original_field.append(list(map(int, input().split())))

for q in range(m):
    for w in range(m):
        for e in range(m):
            if q<w<e:
                arrower.append((q,w,e))

def attack(array,x):
    enemies = array
    attackers = x
    attacked = set()
    for attacks in attackers:
        able_attack = []
        for l in enemies:
            x,y = l[0],l[1]
            long = abs(n-x) + abs(attacks-y)
            if long<=d:
                able_attack.append((long,y,x))
        if not len(able_attack) == 0:
            able_attack.sort()
            attacked.add((able_attack[0][2], able_attack[0][1]))
    return attacked

for A in arrower:
    field = [row[:] for row in original_field]
    result = 0
    while True:
        enemy = []
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if field[i][j] == 1:
                    enemy.append((i, j))
        if len(enemy) == 0:
            break
        attacked_enemy = attack(enemy,A)
        if len(attacked_enemy)>0:
            for k in attacked_enemy:
                enemy_x, enemy_y = k
                field[enemy_x][enemy_y] = 0
                result += 1
        field.pop()
        field.insert(0, [0] * m)
    max_result = max(max_result, result)

print(max_result)