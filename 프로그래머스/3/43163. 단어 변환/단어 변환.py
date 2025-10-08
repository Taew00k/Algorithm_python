from collections import deque

def dfs(word, target, words, visited, word_len, answer):
    if word == target:
        answer_list.append(answer)
    for i in range(len(words)):
        count = 0
        if not visited[i]:
            for x in range(word_len):
                if word[x] == words[i][x]:
                    count += 1
            if count == word_len - 1:
                visited[i] = True
                dfs(words[i], target, words, visited, word_len, answer + 1)
                visited[i] = False                       
    
def solution(begin, target, words):
    global answer_list
    answer_list = []
    if not target in words:
        return 0
    n = len(words)
    word_len = len(words[0])
    visited = [0] * n
    dfs(begin, target, words, visited, word_len, 0)
    return (min(answer_list))