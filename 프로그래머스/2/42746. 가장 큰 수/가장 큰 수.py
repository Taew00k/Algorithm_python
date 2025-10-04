def solution(numbers):
    answer = ''
    new_nums = list(map(str, numbers))
    new_nums = sorted(new_nums, key = lambda x: x*3, reverse=True)
    answer = str(int("".join(new_nums))) 
    return answer