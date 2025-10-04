import math
def solution(brown, yellow):
    size = brown + yellow
    num_list = []
    for i in range(1, int(math.sqrt(size))+1):
        if size%i == 0:
            num_list.append((size//i, i))
    for i in num_list:
        if (i[0] + i[1]) * 2 - 4 == brown:
            return (i[0],i[1])
        