import heapq
def solution(people, limit):
    people.sort()
    left, right, count = 0, len(people)-1, 0
    while left <= right:
        count += 1
        if people[left] + people[right] <= limit:
            right -= 1
            left += 1
        else:
            right -= 1
    return count
        
                
        
        