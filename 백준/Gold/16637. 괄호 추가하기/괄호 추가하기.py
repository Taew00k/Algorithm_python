N = int(input())
math = list(input())
result = -int(1e9)

for i in range(N):
    if i%2 == 0:
        math[i] = int(math[i])

def calculator(num1, num2, s):
    if s== "+":
        return num1+num2
    elif s == "-":
        return num1-num2
    elif s == "*":
        return num1*num2

def dfs(idx, prev):
    global result
    if idx>=N:
        result = max(result, prev)
        return
    if idx+3<N:
        dfs(idx + 4, calculator(prev, calculator(math[idx+1], math[idx+3], math[idx+2]), math[idx]))
    dfs(idx+2, calculator(prev, math[idx+1], math[idx]))

if N == 1:
    result = math[0]
else:
    dfs(1, math[0])

print(result)