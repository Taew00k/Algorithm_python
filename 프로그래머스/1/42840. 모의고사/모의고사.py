def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    score1 = 0
    score2 = 0
    score3 = 0
    for k in range(len(answers)):
        if answers[k] == person1[k%5]:
            score1 += 1
        if answers[k] == person2[k%8]:
            score2 += 1
        if answers[k] == person3[k%10]:
            score3 += 1
    score = [score1, score2, score3]
    
    if max(score) == 0:
        return answer
    
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
            
    return answer