recursion_count = 0
moving_count = 0

n = int(input())
def fib(n):
    global recursion_count
    if n==1 or n==2:
        recursion_count += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

f = [0] * (n+1)

def fibonacci(n):
    global moving_count
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        moving_count += 1
    return f[n]

fib(n)
fibonacci(n)
print(recursion_count,moving_count)