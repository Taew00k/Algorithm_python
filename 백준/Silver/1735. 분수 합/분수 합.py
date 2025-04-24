def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    return int(a*b / gcd(a,b))

c,d = map(int, input().split())
e,f = map(int, input().split())

parent = lcm(d,f)
child = c * parent // d + e * parent//f
print(int(child / gcd(parent, child)), end=" ")
print(int(parent / gcd(parent, child)), end="")