from itertools import product

def solution(word):
    ans_list = []
    count = 0
    alphabet = ['A','E','I','O','U']
    for i in range(1, len(alphabet)+1):
        word_list = [''.join(p) for p in product(alphabet, repeat=i)]
        for k in word_list:
            ans_list.append(k)
    ans_list.sort()
    for x in range(len(ans_list)):
        if ans_list[x] == word:
            return x+1
 