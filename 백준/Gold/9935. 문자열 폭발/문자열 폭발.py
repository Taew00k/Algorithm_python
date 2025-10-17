string = input()
bomb = input()
bomb_len = len(bomb)
stack = []

for ch in string:
    stack.append(ch)
    if len(stack) >= bomb_len:
        if ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:]
            
result = "".join(stack)

if not result:
    print('FRULA')
else:
    print(result)