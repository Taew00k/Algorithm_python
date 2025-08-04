N = int(input())
MAX = -10**9
MIN = 10**9
NUM = list(map(int, input().split()))
CAL = list(map(int, input().split()))
count = 0

def cal(left, right, calculate):
    if calculate == 0:
        return left + right
    elif calculate == 1:
        return left - right
    elif calculate == 2:
        return left * right
    elif calculate == 3:
        if left<0:
            return -(-left//right)
        else:
            return left//right

def dfs(idx, current, calcul):
    global MAX,MIN
    if idx == N:
        if current > MAX:
            MAX = current
        if current < MIN:
            MIN = current
        return

    for i in range(4):
        if calcul[i] > 0:
            next_cal = calcul[:]
            next_cal[i] -= 1
            dfs(idx+1, cal(current, NUM[idx], i), next_cal)

dfs(1, NUM[0], CAL)
print(MAX)
print(MIN)