while True:
    a,b,c = map(int, input().split())
    longest = max(a,b,c)
    total = a+b+c

    if a == b == c == 0:
        break
    elif a == b == c:
        print('Equilateral')
    elif longest >= total-longest:
        print('Invalid')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')