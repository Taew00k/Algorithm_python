n = int(input())
count = 0

if n ==0:
    print(0)
    exit()
    
def Pibonaci(x,y):
    global count
    count +=1
    if count == n:
        return print(y)
    Pibonaci(y, x + y)

Pibonaci(0,1)