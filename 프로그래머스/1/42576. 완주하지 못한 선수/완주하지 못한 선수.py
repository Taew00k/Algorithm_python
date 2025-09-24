def solution(participant, completion):
    member = {}
    for i in range(len(participant)):
        if participant[i] in member:
            member[participant[i]] += 1
        else:
            member[participant[i]] = 1
    for j in range(len(completion)):
        member[completion[j]] -= 1
    for k,v in member.items():
        if v == 1:
            return k
        
        