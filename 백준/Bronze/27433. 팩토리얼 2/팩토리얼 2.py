n = int(input())
total = 1

if n ==0:
    print(1)
    exit()

def factorial(x):
    global total
    total *= x
    x += 1
    if x<=n:
        factorial(x)
    return total

print(factorial(1))