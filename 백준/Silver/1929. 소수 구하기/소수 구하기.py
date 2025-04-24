min_num,max_num = map(int, input().split())

def is_prime(n):
    if n<2:
        return
    for j in range(2,int(n**0.5)+1):
        if n % j == 0:
            return
    return print(n)

for i in range(min_num, max_num+1):
    is_prime(i)
