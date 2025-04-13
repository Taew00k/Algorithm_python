n = int(input())

row = 3
for i in range(n-1):
    row += pow(2,i+1)

print(row*row)