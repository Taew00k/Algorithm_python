def solution(n, times):
    min_times = 1
    max_times = max(times) * n
    while min_times <= max_times :
        count = 0
        middle = (min_times + max_times) // 2
        for i in times:
            count += (middle // i)
        if count >= n:
            answer = middle
            max_times = middle - 1
        else:
            min_times = middle + 1
    return answer
            