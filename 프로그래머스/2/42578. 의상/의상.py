def solution(clothes):
    clothes_type = {}
    answer = 1
    for i in clothes:
        if i[1] not in clothes_type:
            clothes_type[i[1]] = 2
        else:
            clothes_type[i[1]] += 1
    for j in clothes_type.values() :
        answer *= j
    return answer-1