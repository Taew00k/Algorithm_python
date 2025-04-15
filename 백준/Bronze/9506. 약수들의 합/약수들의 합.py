while True:
    n = int(input())
    numbering = []
    count = 0
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n % i == 0:
                count += i
                numbering.append(i)
        if n == count:
            print(f'{n} = ', end='')
            for i in range(len(numbering)):
                if i == 0:
                    print(f'{numbering[i]}', end='')
                else:
                    print(f' + {numbering[i]}', end='')
            print()
        else:
            print(f'{n} is NOT perfect.')