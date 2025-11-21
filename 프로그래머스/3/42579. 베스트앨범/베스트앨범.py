from collections import defaultdict
def solution(genres, plays):
    diction = defaultdict(list)
    music = list(enumerate(list(zip(genres, plays))))
    play_dict = {}
    genres = []
    for m in music:
        if m[1][0] in play_dict:
            play_dict[m[1][0]] += m[1][1]
        else:
            play_dict[m[1][0]] = m[1][1]
    for k,v in play_dict.items():
        genres.append((k,v))
    genres.sort(key = lambda x: -x[1])
    for m in music:
        diction[m[1][0]].append((m[0], m[1][1]))
    for k,v in diction.items():
        diction[k].sort(key = lambda x: (-x[1], x[0]))
    answer = []
    for g in genres:
        key = g[0]
        count = min(2, len(diction[key]))
        for i in range(count):
            answer.append(diction[key][i][0])
    return answer
    