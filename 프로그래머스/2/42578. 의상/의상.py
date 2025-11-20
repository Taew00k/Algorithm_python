from collections import defaultdict
def solution(clothes):
    sum = 1
    blanket = defaultdict(list)
    for c in clothes:
        blanket[c[1]].append(c[0])
    for k,v in blanket.items():
        sum *= (len(blanket[k]) + 1)
    return sum - 1
        
