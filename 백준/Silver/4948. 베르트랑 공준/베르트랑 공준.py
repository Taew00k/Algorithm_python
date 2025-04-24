def is_prime(x):
    if x<2:
        return False
    for j in range(2,int(x**0.5)+1):
        if x%j == 0:
            return False
    return x

while True:
    n = int(input())
    answer=[]
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if is_prime(i):
            answer.append(is_prime(i))
    print(len(answer))