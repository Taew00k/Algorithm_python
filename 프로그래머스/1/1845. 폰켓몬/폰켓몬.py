def solution(nums):
    length = len(nums) // 2
    a = set([])
    for n in nums:
        if not n in a:
            a.add(n)
        if len(a) == length:
            break
    return len(a)
        
    