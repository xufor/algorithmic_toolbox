def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)
    # return gcd(a % b, b) wont work
    # return gcd(a % b, a) wont work

a, b = map(int, input().split())
print(int(a*b/gcd(a, b)))