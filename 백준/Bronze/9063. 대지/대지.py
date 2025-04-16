n = int(input())
array_x = []
array_y = []

for _ in range(n):
    x,y = map(int,input().split())
    array_x.append(x)
    array_y.append(y)

array_x.sort()
array_y.sort()

length = array_x[len(array_x)-1] - array_x[0]
height = array_y[len(array_x)-1] - array_y[0]

if n == 1:
    print(0)
else:
    print(length * height)