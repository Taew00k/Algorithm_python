x, y, w, h = map(int,input().split())
distance = x - 0

if w - x < distance:
    distance = w-x
if y - 0 < distance:
    distance = y-0
if h - y < distance:
    distance = h - y

print(distance)