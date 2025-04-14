import math

a, b, v = map(int,input().split())
one_day = a-b
day = math.ceil((v-a)/(a-b)) + 1

print(day)