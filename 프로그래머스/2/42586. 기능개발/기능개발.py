import math

def solution(progresses, speeds):
    answer = []
    progressing = []
    time = 0
    for i in range(len(progresses)):
        if math.ceil((100 - progresses[i]) / speeds[i]) > time:
            time = math.ceil((100 - progresses[i]) / speeds[i])
            if progressing:
                answer.append(len(progressing))
            progressing = [progresses[i]]
        else:
            progressing.append(progresses[i])
            
    if progressing:
        answer.append(len(progressing))
    
    return answer