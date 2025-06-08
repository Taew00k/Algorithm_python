from collections import deque
t = int(input())

for _ in range(t):
    happy = False
    store = []
    n = int(input())
    visited = [0] * (n+2)
    for _ in range(n+2):
        store.append(list(map(int, input().split())))
    if abs(store[len(store)-1][0]-store[0][0]) + abs(store[len(store)-1][1]-store[0][1]) <= 1000:
        print("happy")
        happy = True
    else:
        queue = deque()
        queue.append((store[0][0],store[0][1]))
        while queue:
            start_x, start_y = queue.popleft()
            if start_x == store[len(store)-1][0] and start_y == store[len(store)-1][1]:
                print("happy")
                happy = True
                break
            else:
                for i in range(1,n+2):
                    if abs(store[i][0] - start_x) + abs(store[i][1] - start_y)<=1000 and visited[i] == 0:
                        queue.append((store[i][0], store[i][1]))
                        visited[i] = 1
        if not happy:
            print("sad")
