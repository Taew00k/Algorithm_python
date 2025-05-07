n, m = map(int, input().split())
result = []
count = 0

def backtracking():
    if len(result) == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    for j in range(1,n+1):
        if len(result)>0:
            if result[-1] <= j:
                result.append(j)
                backtracking()
                result.pop()
        elif len(result) ==0 :
            result.append(j)
            backtracking()
            result.pop()

backtracking()