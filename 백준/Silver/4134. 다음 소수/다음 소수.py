n = int(input())

def is_prime(a):
    if a<2:
        return False
    for j in range(2, int(a**0.5)+1):
        if a % j == 0:
            return False
    return True

for _ in range(n):
    x = int(input())
    i = x
    while True:
        check = is_prime(i)
        if check:
            print(i)
            break
        i += 1