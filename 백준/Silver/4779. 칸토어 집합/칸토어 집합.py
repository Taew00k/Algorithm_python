def change(a, n):
    if n == 1:
        return
    for i in range(a + n // 3, a + n//3 *2):
        string[i] = ' '
    change(a, n//3)
    change(a+n//3*2, n//3)

import sys
while True:
    try :
        N = int(sys.stdin.readline())
        string = ['-']*(3**N)
        change(0,3**N)
        print(''.join(string))
    except:
        break
