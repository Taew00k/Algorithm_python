N = int(input())
tree = []
gap_set = []

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

for _ in range(N):
    tree.append(int(input()))

for i in range(1, len(tree)):
    gap = tree[i] - tree[i-1]
    gap_set.append(gap)

count = gap_set[0]

for i in range(1,len(gap_set)):
    count = gcd(count, gap_set[i])

print((max(tree)-min(tree)) // count - N + 1)