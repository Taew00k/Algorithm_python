n,m = map(int, input().split())
result = []

def backtracking():
    if len(result) == m:
        for i in result:
            print(i, end=" ")
        print()
        return
    for j in range(1,n+1):
        result.append(j)
        backtracking()
        result.pop()

backtracking()
