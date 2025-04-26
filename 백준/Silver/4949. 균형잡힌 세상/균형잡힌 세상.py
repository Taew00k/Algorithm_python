while True:
    string = list(input())
    signal = []
    if string[0] == ".":
        break
    for i in string:
        if i == "(":
            signal.append(i)
        elif i == "[":
            signal.append(i)
        elif i == ")":
            if len(signal) > 0 and signal[len(signal)-1] == "(":
                signal.pop()
            else:
                print('no')
                break
        elif i == "]":
            if len(signal) > 0 and signal[len(signal)-1] == "[":
                signal.pop()
            else:
                print('no')
                break
        elif i == ".":
            if len(signal) == 0:
                print('yes')
            else:
                print('no')
            break