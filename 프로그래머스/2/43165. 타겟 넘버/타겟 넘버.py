def solution(numbers, target):
    num_list = []
    count = 0
    
    for n in numbers:
        num_list.append((n,-n))
        
    def dfs(idx, total):
        nonlocal count
        if idx == len(numbers):
            if total == target:
                count += 1
            return
        dfs(idx+1, total + num_list[idx][0])
        dfs(idx+1, total + num_list[idx][1])
        
    dfs(0,0)
    return count