import math
import itertools

def isPrime(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
                   

def solution(numbers):
    count = 0
    answer = []
    real_num = set()
    list_num = list(map(str, numbers))
    for i in range(1, len(list_num)+1):
        for perm in itertools.permutations(list_num, i):
            num = int("".join(perm))
            real_num.add(num)

    for j in real_num:
        if isPrime(j):
            count += 1
    return count
        
        