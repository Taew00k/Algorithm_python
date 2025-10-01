def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    answer = []
    for i, (g,p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [[p,i]]
        else:
            dic1[g].append([p,i])
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
            
    for g1, v1 in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for y2 in sorted(dic1[g1], key=lambda x:(-x[0],x[1]))[:2]:
            answer.append(y2[1])
            
    return answer
        
        
        