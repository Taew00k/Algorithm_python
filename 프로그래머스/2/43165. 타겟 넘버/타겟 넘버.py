from collections import deque

def dfs(new_num, num, visited, total, count, final, ans):
    if count == num:
        if total == final:
            ans += 1
        return ans
    
    for i in range(2):
        if not visited[count][i]:
            visited[count][i] = True
            ans = dfs(new_num, num, visited, total + new_num[count][i], count + 1, final, ans)
            visited[count][i] = False
            
    return ans
            
def solution(numbers, target):
    new_num = []
    n = len(numbers)
    for i in numbers:
        new_num.append([i, -i])
    visited = [[0] * 2 for _ in range(n)]
    return dfs(new_num, n, visited, 0, 0, target, 0)
    
    