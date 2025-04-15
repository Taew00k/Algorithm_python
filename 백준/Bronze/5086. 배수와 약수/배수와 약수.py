while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    elif n > m:
        if n % m == 0:
            print('multiple')
        else:
            print('neither')
    elif n < m:
        if m % n == 0:
            print('factor')
        else:
            print('neither')