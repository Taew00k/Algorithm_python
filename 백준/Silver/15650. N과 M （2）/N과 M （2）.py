n,m = map(int, input().split())
result = []
check = []

def backtracking():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in range(1,n+1):
        if i not in result:
            if len(result)==0 or i>result[-1]:
                result.append(i)
                backtracking()
                result.pop()
backtracking()