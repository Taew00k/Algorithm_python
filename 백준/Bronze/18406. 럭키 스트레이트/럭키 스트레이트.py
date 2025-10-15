N = str(input())
start = N[:(len(N)//2)]
end = N[len(N)//2:]
first = []
last = []
for i in start:
    first.append(int(i))
for j in end:
    last.append(int(j))
if sum(first) == sum(last):
    print('LUCKY')
else:
    print('READY')