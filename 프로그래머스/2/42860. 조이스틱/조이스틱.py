def solution(name):
    answer = 0
    n = len(name)
    move = n-1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        move = min(move, i*2 + n - next_idx)
        move = min(move, (n-next_idx) * 2 + i)

    answer += move
    return answer
                