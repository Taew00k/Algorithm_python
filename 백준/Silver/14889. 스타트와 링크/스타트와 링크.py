N = int(input())
team = []
visited = [0] * N
for i in range(N):
    team.append(list(map(int, input().split())))
result = 10**9

def dfs(a, idx):
    global result
    if a == N/2:
        team_start = 0
        team_link = 0
        for x in range(N):
            for y in range(N):
                if visited[x] and visited[y]:
                    team_start += team[x][y]
                elif not visited[x] and not visited[y]:
                    team_link += team[x][y]
        if abs(team_start-team_link) < result:
            result = abs(team_start-team_link)
        return
    else:
        for k in range(idx, N):
            if not visited[k]:
                visited[k] = True
                dfs(a + 1, k + 1)
                visited[k] = False

dfs(0,0)
print(result)