n = int(input())
switch_list = list(map(int, input().split()))
p = int(input())

for _ in range(p):
    s,idx = map(int, input().split())
    if s == 1:
        for i in range(idx-1, n, idx):
            if switch_list[i] == 0:
                switch_list[i] = 1
            else:
                switch_list[i] = 0
    elif s == 2:
        if switch_list[idx-1] == 0:
                switch_list[idx-1] = 1
        else:
            switch_list[idx-1] = 0
        left_switch = switch_list[:idx-1]
        right_switch = switch_list[idx:]
        count = 1
        while True:
            if not left_switch or not right_switch or not left_switch[-1] == right_switch[0]:
                break
            else:
                if left_switch[-1] == 0:
                    switch_list[idx-1-count] = 1
                    switch_list[idx-1+count] = 1
                else:
                    switch_list[idx-1-count] = 0
                    switch_list[idx-1+count] = 0
            count += 1
            left_switch.pop()
            right_switch.pop(0)
    
for i in range(n):
    print(switch_list[i], end=" ")
    if (i + 1) % 20 == 0:
        print()