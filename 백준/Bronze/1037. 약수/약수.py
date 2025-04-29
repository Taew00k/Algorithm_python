n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(a[0]**2)
else:
    print(a[0]*a[-1])