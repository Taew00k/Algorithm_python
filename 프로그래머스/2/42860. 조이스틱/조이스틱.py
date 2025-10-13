def solution(name):
    up_alphabet = ['','B','C','D','E','F','G','H','I','J','K','L','M']
    low_alphabet = ['','Z','Y','X','W','V','U','T','S','R','Q','P','O','N']
    all_a = "A" * len(name)   
    total = -1
    for i in range(len(name)):
        if name[i] == 'A':
            continue
        else:
            total += 1
            if name[i] > 'M':
                for k in range(14):
                    if name[i] == low_alphabet[k]:
                        total += k
            else:
                for k in range(13):
                    if name[i] == up_alphabet[k]:
                        total += k
    return total
                
                