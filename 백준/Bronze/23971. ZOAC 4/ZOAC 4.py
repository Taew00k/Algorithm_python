import math
h,w,n,m = map(int, input().split())

height = math.ceil(h/(n+1))
width = math.ceil(w/(m+1))

print(height * width)