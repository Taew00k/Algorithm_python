import heapq

def solution(operations):
    op_list = []
    op_reverse = []
    for o in operations:
        a,b = o.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(op_list, b)
            heapq.heappush(op_reverse, -b)
        elif a == 'D':
            if b == -1:
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