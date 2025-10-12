import heapq

def solution(operations):
    op_list = []
    op_reverse = []
    for operate in operations:
        a,b = map(str, operate.split())
        if a == 'I':
            heapq.heappush(op_list, int(b))
            heapq.heappush(op_reverse, -int(b))
        elif a == 'D':
            if int(b) == -1:
                if len(op_list) > 0:
                    x = heapq.heappop(op_list)
                    op_reverse.remove(-x)
            else:
                if len(op_reverse) > 0:
                    x = heapq.heappop(op_reverse)
                    op_list.remove(-x)
    if len(op_reverse) < 1:
        max_num = 0
    else:
        max_num = -heapq.heappop(op_reverse)
    if len(op_list) < 1:
        min_num = 0
    else:
        min_num = heapq.heappop(op_list)
        
    return (max_num, min_num)