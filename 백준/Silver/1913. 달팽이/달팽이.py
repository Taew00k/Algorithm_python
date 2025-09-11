n = int(input())
num = int(input())
arr = [[0] * n for _ in range(n)]
now = n*n
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x = 0
y = 0
d = 0
ax = 0
ay = 0

while now > 0:
      arr[x][y] = now
      if now == num:
            ax = x+1
            ay = y+1
      now -= 1
      nx = x+dx[d]
      ny = y+dy[d]

      if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny] != 0:
            d = (d+1) % 4

      x = x + dx[d]
      y = y + dy[d]

for i in range(len(arr)):
      for j in range(len(arr[0])):
          print(arr[i][j], end=" ")
      print()

print(ax,ay)
