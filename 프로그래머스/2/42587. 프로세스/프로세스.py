from collections import deque

def solution(priorities, location):
    new_priorities = deque()
    count = 0
    
    for i in range(len(priorities)):
        new_priorities.append((i, priorities[i]))
        
    while new_priorities:
        b = new_priorities.popleft()
        if b[1] >= max(priorities):
            count += 1
            priorities.remove(b[1])
            if b[0] == location:
                return count
        else:
            new_priorities.append(b)